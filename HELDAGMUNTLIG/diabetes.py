import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("diabetes.csv")
#print(df.head(3))
#print(list(df.columns.values))
#print(df["Diabetes_binary"])

smokeCheck = df[df["Smoker"] == 1]
# print(smokeCheck)

smoking_diabetes = smokeCheck["Diabetes_binary"].value_counts().sort_index()
print(smoking_diabetes)

diabetesCheck = df["Diabetes_binary"].value_counts()
# print(diabetesCheck)




# preDiabetes = df[df["Diabetes_binary"] == 1] 
