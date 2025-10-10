import pickle
import pandas as pd

f = open("../model/decisiontree.pkl", "rb")
model = pickle.load(f)
f.close()
ref_code = pd.read_csv("../model/referee_encoding.csv")
label = ["xg", "xga", "ref_encode"]


def predict(xg: float, xga: float, ref_name: str):
    # ค้นหารายชื่อกรรมการแล้วนำไป map เป็นตัวเลขตามไฟล์ ref csv
    ref_code = matchRef(ref_name)
    df = pd.DataFrame([[xg, xga, ref_code]], columns=label)

    # หาค่าความเป็นไปได้ทั้งหมด
    prob = model.predict_proba(df)
    columns = model.classes_
    probs_df = pd.DataFrame(prob, columns=columns)
    return probs_df.to_dict()


def matchRef(ref_name) -> int:
    """
    this function will match name ref with code in referee_encoding.csv to get code for prediction
    """
    code = ref_code[ref_code["referee"] == ref_name]["code"].values[0]
    return code


def getRef(ref=ref_code) -> list[dict]:

    return ref["referee"].to_dict()


print(getRef())
