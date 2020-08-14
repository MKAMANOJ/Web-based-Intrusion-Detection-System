# Intrusion Detection System

It is an web-based attack detection system using the CSIC 2010 HTTP datatsets. Uses features extraction and reduction techniques to reduce dimension of the Dataset and two techniques to build the attack detection model. 1) SVM model  2) Probabalistic Model Using Naives Bayes

## Requirements
* Python 2
* Numpy
* Scipy
* Scikit-Learn 
* Nltk
* Gtk


## Naive Model - Project Structure

1. Datasets : Contains CSIC datasets

* 1.1) originalDatasets: Datasets without pre-processing

* 1.2) naive : Contains extractNaive.py which processes original Datasets to extract only data payloads headers

Usage: python3 extractNaive.py inputfile   outputfile

Repeat for normal and anomalous datasets.

* 1.3) processed Dataset: Dataset after preprocessing i.e. getting only the header payload after 1.2

1.3.1) k-fold : Contains kFold.py which divides processed datasets into training and test sets

Usage: python3 kFold.py filename

Repeat for normal and anomalous datasets.

1.3.2) test and training folders contains datasets testing and training respectively.


2. Models: Contains Models developed using the Naives Bayes method

* 2.1) naiveModel.py : It build the model using training datasets from the Datasets Folder

Usage: python3 naiveModel.py

* 2.2) test_naive_classifier.py : To test the model aainst a single war input

Usage: python test_naive_classifier.py <some test strings follows>

* 2.3) model_accuracy.py : It calculates the accuracy of the model against the test datasets in the datasets folder.

3. Application

* 3.1. live_test.py and nids.py : Gui application that shows anamolous and normal http packet flowing the network

Usage: sudo python3 nids.py

* 3.2) models : Contains models

* 3.3) logs: contains log files created during different instances of the nids applicaton

## SVM
run_svm.sh : It can be used to run the whole steps for svm -  preprocessing to predicting accuracy.

Usage: bash run_svm.sh

1. extractFeaturesFromDataset.py: Applies pre-processing to dataset to abstract only the required features.

Usage:

python3 extractFeaturesFromDataset.py normal.txt

python3 extractFeaturesFromDataset.py anomalous.txt

2. convert_txt_to_csv.py : Converts the extracted features to csv files

Usage:

python3 convert_txt_to_csv.py normalFeatureExtracted.txt

python3 convert_txt_to_csv.py anomalousFeatureExtracted.txt


3. svm.py: Performs svm and calculates the accuracy

python3 svm.py normalFeatureExtracted.csv anomalousFeatureExtracted.csv