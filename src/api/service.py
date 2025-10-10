import pickle
import pandas as pd

f = open("../model/decisiontree.pkl", "rb")
ref_code = pd.read_csv("../model/referee_encoding.csv")
model = pickle.load(f)
f.close()


def predict(xg: float, xga: float, ref_name: str):
    ref_code = matchRef(ref_name)
    df = pd.DataFrame([[xg, xga, ref_code]])
    prob = model.predict_proba()
    columns = model.classes_
    probs_df = pd.DataFrame(prob, columns=columns)
    print()


def matchRef(ref_name) -> int:
    """
    this function will match name ref with code in referee_encoding.csv to get code for prediction
    """

    print(ref_code[ref_code["referee"] == ref_name].code[0])
