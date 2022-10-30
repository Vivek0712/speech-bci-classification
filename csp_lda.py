if __name__ == "__main__":

    ############################################# Imports, Loads, Defines ################################################################
    from mne.decoding import CSP
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    from sklearn.model_selection import StratifiedKFold
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import classification_report, confusion_matrix
    import numpy as np
    import json
    import pickle
    import sys
    
    test_set_size = 0.1
    n_validation_splits = 5
    n_csp_components = 32
    
    scaler = StandardScaler()
    
    subject = sys.argv[1]
    
    print(f"Subject - {subject}")
    
    X = np.load(f"X_{subject}.npy")
    Y = np.load(f"Y_{subject}.npy")
    
    class_map = {0:"Inner", 1:"Pronounced", 2:"Visualized"}
    
    ############################################# Classifier Training ################################################################
    
    classifier = {}
    classifier['num_classifiers'] = n_validation_splits

    cv = StratifiedKFold(n_splits=n_validation_splits, shuffle=True)

    #out-of-fold predictions for validation data created during the splits
    y_oof_preds = np.empty(len(Y))

    for split, (train_idx, valid_idx) in enumerate(cv.split(X, Y)):
        
        print(f"split no. - {split+1}")

        lda = LinearDiscriminantAnalysis()
        csp = CSP(n_components=n_csp_components, reg=None, log=True)

        trainX, trainY = X[train_idx], Y[train_idx]
        validX, validY = X[valid_idx], Y[valid_idx]

        train_features = csp.fit_transform(trainX, trainY)
        valid_features = csp.transform(validX)

        lda.fit(train_features, trainY)
        y_oof_preds[valid_idx] = lda.predict(valid_features)

        classifier[f'csp_{split}'] = csp
        classifier[f'lda_{split}'] = lda


    validation_classifier_report = classification_report(Y, y_oof_preds, labels=list(class_map.keys()), target_names=list(class_map.values()), output_dict=True)
    validation_classifier_conf_matrix = confusion_matrix(Y, y_oof_preds)

    classifier['validation_data_classification_report'] = validation_classifier_report
    classifier['validation_data_confusion_matrix'] = validation_classifier_conf_matrix

    with open(f'classifier_{subject}.pickle', 'wb') as handle:
        pickle.dump(classifier, handle, protocol=pickle.HIGHEST_PROTOCOL)

    print("classifier validation metrics:\n", classifier['validation_data_classification_report'], end='\n')