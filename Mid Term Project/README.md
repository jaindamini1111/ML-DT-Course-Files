# Autism_Screening

Autistic Spectrum Disorder (ASD) is a neurodevelopment condition associated with significant healthcare costs, and early diagnosis can significantly reduce these. Unfortunately, waiting times for an ASD diagnosis are lengthy and procedures are not cost effective. The economic impact of autism and the increase in the number of ASD cases across the world reveals an urgent need for the development of easily implemented and effective screening methods. Therefore, a time-efficient and accessible ASD screening is imminent to help health professionals and inform individuals whether they should pursue formal clinical diagnosis. The rapid growth in the number of ASD cases worldwide necessitates datasets related to behaviour traits. However, such datasets are rare making it difficult to perform thorough analyses to improve the efficiency, sensitivity, specificity and predictive accuracy of the ASD screening process. Presently, very limited autism datasets associated with clinical or screening are available and most of them are genetic in nature. Hence, we propose a new dataset related to autism screening of adults that contained 20 features to be utilised for further analysis especially in determining influential autistic traits and improving the classification of ASD cases. In this dataset, we record ten behavioural features (AQ-10-Adult) plus ten individuals characteristics that have proved to be effective in detecting the ASD cases from controls in behaviour science.

Source:Fadi Fayez Thabtah
Department of Digital Technology
Manukau Institute of Technology,
Auckland, New Zealand
fadi.fayez@manukau.ac.nz

https://www.kaggle.com/faizunnabi/autism-screening


### EDA is present in notebook
Steps to reproduce - Start a juypter kernel and run the notebook.

### Model training with hyperparamter tuning is also present in the notebook
Steps to reproduce - Same as above.

### Exporting notebook to script - train.py

### Model deployment is done with Flask - predict.py
Steps to run - Open a terminal and type: `python predict.py` You will get a screen which asks you to upload a file, Please upload testautism.csv as the uploading file and click on submit to fetch results.

### Dependency and enviroment management - requirements.txt

### Containerization - Dockerfile
Steps to build docker image - `docker build -t give_any_name_you_like .`
Steps to run docker - `docker run -it -p 6969:6969 give_the_name_you_gave_above_while_buildingdocker`

### Cloud deployment - No deployment is done on the cloud.

