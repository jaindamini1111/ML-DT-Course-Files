import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import roc_auc_score
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

def train_xgbclassifier(x_ros, y_ros, X_valid, y_valid, X_test, y_test):
    """With our tuned parameters train a random forest model."""

    xgb_model = XGBClassifier(objective = "multi:softmax", random_state = 42, subsample = 0.5,
 n_estimators = 1500, min_child_weight = 1, max_depth = 3, learning_rate = 0.005, colsample_bytree = 1.0)
    xgb_model.fit(x_ros, y_ros)
    
    validxgb_predproba = xgb_model.predict_proba(X_valid)
    xgb_predproba = xgb_model.predict_proba(X_test)
    y_test = y_test.squeeze()
    y_valid = y_valid.squeeze()
    print("ROC-AUC score of model on validation set: {0}".format(roc_auc_score(y_valid, validxgb_predproba, multi_class='ovo', average='weighted')))
    print("ROC-AUC of model on test set: {0}".format(roc_auc_score(y_test, xgb_predproba, multi_class='ovo', average='weighted')))
    
    pickle.dump(xgb_model, open("xgbclassifier_tuned.pkl", "wb"), pickle.HIGHEST_PROTOCOL)
              
     
              
def main():
    X, y = read_csv()
    X_train, y_train, X_valid, y_valid, X_test, y_test = split_dataset(X = X, y = y)  
    x_ros, y_ros = resolve_imbalanced_data(X_train = X_train, y_train = y_train)
    train_xgbclassifier(x_ros = x_ros, y_ros = y_ros, X_valid = X_valid, y_valid = y_valid, X_test = X_test, y_test = y_test)
              
              
              
if __name__ == "__main__":
    main()