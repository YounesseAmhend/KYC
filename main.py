import pandas as pd
from ydata_profiling import ProfileReport
from sklearn.preprocessing import LabelEncoder


# les variables de l'encodage
to_num = ["nameDest", "nameOrig", "type"]

df_fraud = pd.read_csv("csv/Fraud.csv")
df_fraud_encode = pd.read_csv("Fraud.csv", usecols=to_num)
# pour analyser la base de données

"""profile = ProfileReport(df_fraud, infer_dtypes=False,  lazy=False)
profile.to_file("analyses.html")"""

# encodage 
le = LabelEncoder()
encodingKey = []

for i in to_num:
    #encodage pour chaque column 
    df_fraud[i] = pd.to_numeric(le.fit_transform(df_fraud[i].astype(str)))
    key = df_fraud[i].unique()
    temp = []
    count = 0
    # juste pour stocker les valeurs donné par la fonction d'encodage
"""    if i in ["nameDest", "nameOrig"]:
        continue
    for row in df_fraud_encode[i].unique():
        temp.append({f"{key[count]}": row})
        count += 1
    encodingKey.append({i: temp})

with open("json/encodingKey.json", "w") as f:
    f.write("[\n")
    for i in range(len(encodingKey)):
        if i != len(encodingKey)-1:
            f.write(str(encodingKey[i]).replace(
                "\'", "\"").replace("nan", "\"\"")+",\n")
        else:
            f.write(str(encodingKey[i]).replace(
                "\'", "\"").replace("nan", "\"\"")+"\n")
    f.write("]")
    f.close()"""

df_fraud.to_csv("csv/encoded_fraud.csv")