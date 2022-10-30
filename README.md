# speech-bci-classification
This Project is part of NTX Hackathon 2022

Original Code and Dataset: https://github.com/N-Nieto/Inner_Speech_Dataset/

Objective: Evaluate the best pre-processing and Classifier methods to classify EEG data into three classes - `Inner Speech`, `Pronounced Speech` and `Visual Condition`

Method of Implementation

- Extract the features from the dataset
- Reduce the dimensionlity of the data using the following methods
  - Principal Component Analysis (PCA)
  - Common Spatial Filters (LDA)
  
- Classify the data using Classification models
    - Use Automated Machine Learning to get the best preprocessing and classifier model
    - Other classifier models - Linear Discriminant Analysis (LDA)
 
RESULTS:
| METHOD OF IMPLEMENTATION | Algorithm |	ACCURACY |	F1 Score |
-----------------------------------------------------------------
PCA + AutoML	|PCA, MinMaxScaler, ExtremeRandomTrees |	41.31%	| 0.03711 |
CSP + LDA| 	CSP + LDA	| 52.15%	| 0.5215|
CSP + AUTOML |CSP,TruncatedSVDWrapper,XGBoostClassifier| 	79.45%	| 0.7933 |
