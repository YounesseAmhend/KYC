import pandas as pd

from sklearn.neural_network import MLPClassifier

from sklearn.model_selection import train_test_split

from table_logger import TableLogger

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

import joblib

variables = [ "step", "type", "amount", "nameOrig","oldbalanceOrg", "newbalanceOrig", "nameDest",

             "oldbalanceDest", "newbalanceDest", "isFraud"

            ]

tb = TableLogger(columns='method,Accuracy,Precision,Recall,F1_score',
                    default_colwidth=9,
                    float_format='{:,.2f}'.format)

# Train the model on the training data

df = pd.read_csv("csv/encoded_fraud.csv", usecols=variables)

# stocker tous les variables et sont valeur dans X sauf isFraud

X = df.drop("isFraud", axis=1)

# stocker les valeurs de isFraud dans y

y = df["isFraud"]


# diviser les données en ensembles d'apprentissage et de test

X_train, X_test, y_train, y_test = train_test_split(X, y)


# initialisation du modèle

model = MLPClassifier(hidden_layer_sizes=(10,), activation='relu', solver='adam', max_iter=4000)


# Entraînement du modèle

model.fit(X_train, y_train)
    

# Évaluation du modèle

y_pred = model.predict(X_test)


print(" accuracy : {:.2f}".format(accuracy_score(y_test, y_pred)*100) + " %\n", 

      "precision score : {:.2f}".format(precision_score(y_test, y_pred)*100) + " %\n",

      "recall score : {:.2f}".format(recall_score(y_test, y_pred)*100) + " %\n",

      "f1 score : {:.2f}".format(f1_score(y_test, y_pred)*100)+ " %\n"
    )
tb(
    "ANN",
    "{:.2f}".format(accuracy_score(y_test, y_pred)*100) + " %", 
    "{:.2f}".format(precision_score(y_test, y_pred)*100) + " %",
    "{:.2f}".format(recall_score(y_test, y_pred)*100) + " %",
    "{:.2f}".format(f1_score(y_test, y_pred)*100)+ " %"
)
# fermer le tableau
tb.print_line(("+"+"-"*11)*5+"+")

# exporter le modèle

joblib.dump(model, 'models/is_fraud.joblib')