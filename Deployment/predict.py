import pickle
import requests




def import_model(file_path):
    """Imports the trained classifier."""
    
    with open(file_path, "rb") as inp:
        trained_model = pickle.load(inp)

    return trained_model




def main():
    dictvect = import_model(file_path = "dv.bin")
    trainedmodel = import_model(file_path = "model1.bin")
    customer = {"contract": "two_year", "tenure": 12, "monthlycharges": 19.7}
    X = dictvect.transform([customer])
    print(trainedmodel.predict_proba(X)[0, 1])
    
    
    
if __name__ == "__main__":
    main() 
        