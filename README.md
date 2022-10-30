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
    
 Dataset :
 
- We have used Inner speech dataset by OpenNeuro. Data were acquired using BioSemi ActiveTwo high resolution biopotential measuring system.​
- Channels - 128 active EEG and 8 active EOG/EMG​
- Resolution - 28 bits, Sampling rate -1024 Hz​
- This dataset contains ten healthy right-handed participants with mean age 34. 

RESULTS:

- Following is the comparison of metrics over cross-subject data trained with various methods

| METHOD OF IMPLEMENTATION | Algorithm |	ACCURACY |	F1 Score |
| ------------------------- | --------- | --------- | ------------ |
PCA + AutoML	|PCA, MinMaxScaler, ExtremeRandomTrees |	41.31%	| 0.03711 |
CSP + LDA| 	CSP + LDA	| 52.15%	| 0.5215|
CSP + AUTOML |CSP,TruncatedSVDWrapper,XGBoostClassifier| 	79.45%	| 0.7933 |

![Overall_f1](https://user-images.githubusercontent.com/47343923/198880777-3a1e75ac-3703-4ea1-ae3e-e1e7a99f4851.png)
![Overall_accuracy](https://user-images.githubusercontent.com/47343923/198880787-2832951f-3cd2-48ad-88ef-545310b738b4.png)

- Results of CSP + LDA methods

![Accuracy](https://user-images.githubusercontent.com/47343923/198880804-fd1445d7-a480-4ad6-8554-a3a6f5dcb096.png)
![Precision](https://user-images.githubusercontent.com/47343923/198880817-5435ac14-7e4b-470b-8abb-453a5d1cd701.png)
![Recall](https://user-images.githubusercontent.com/47343923/198880829-97948b99-5907-42cb-a579-fffcde2d43d0.png)
![F1](https://user-images.githubusercontent.com/47343923/198880837-ca2c5c42-f97d-4595-9bc6-b83608d2f939.png)
