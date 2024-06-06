from pandas import read_csv
from sklearn.tree import DecisionTreeClassifier

giocatori=read_csv("giocatori.csv")
X=giocatori.drop(columns=["videogame"])
y=giocatori["videogame"]

modello=DecisionTreeClassifier()
modello.fit(X.values, y.values)
sesso=input("il tuo sesso:  ")
if sesso=="maschio":
    sesso=1
if sesso=="femmina":
    sesso=0
eta=int(input("la tua età: "))
previsioni = modello.predict([[sesso, eta]])
print(previsioni)