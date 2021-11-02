import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import imblearn
import pickle



def read_csv():
    """Import the preprocessed X and y csv's."""

    X = pd.read_csv("X.csv")
    y = pd.read_csv("y.csv")

    return X, y
    

def split_dataset(X, y):
    """Split the X and y into train, valid & test sets."""
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle = True, test_size = 0.2, random_state=42, stratify = y)
    X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train, shuffle = True, test_size = 0.2, random_state=42, stratify = y_train)

    return X_train, y_train, X_valid, y_valid, X_test, y_test

    
def resolve_imbalanced_data(X_train, y_train):
    """Using SMOTE resolve imbalanced classes for y."""
    
    ros = imblearn.over_sampling.RandomOverSampler(random_state=42)
    x_ros, y_ros = ros.fit_resample(X_train, y_train)
    
    return x_ros, y_ros

def train_random_forest(x_ros, y_ros, X_valid, y_valid, X_test, y_test):
    """With our tuned parameters train a random forest model."""

    rf = RandomForestClassifier(random_state = 42,  max_depth = 9, min_samples_leaf = 1, min_samples_split = 2, n_estimators =  500)
    rf.fit(x_ros, y_ros)

    print("Accuracy of model on validation set: {0}".format(accuracy_score(y_valid, rf.predict(X_valid))))
    print("Accuracy of model on test set: {0}".format(accuracy_score(y_test, rf.predict(X_test))))
    
    pickle.dump(rf, open("randomforest_tuned.pkl", "wb"), pickle.HIGHEST_PROTOCOL)
              
     
              
def main():
    X, y = read_csv()
    X_train, y_train, X_valid, y_valid, X_test, y_test = split_dataset(X = X, y = y)  
    x_ros, y_ros = resolve_imbalanced_data(X_train = X_train, y_train = y_train)
    train_random_forest(x_ros = x_ros, y_ros = y_ros, X_valid = X_valid, y_valid = y_valid, X_test = X_test, y_test = y_test)
              
              
              
if __name__ == "__main__":
    main()
              
