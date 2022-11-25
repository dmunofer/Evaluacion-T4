import csv
import pandas as pd

df = pd.read_csv("Pokemon.csv")

def mostrarPokenumero(npoke):
    return df.loc[df['#']==npoke]

def mostrarPokenombre(nombre):
    lista=df[df['Name']==nombre].index.tolist()
    for indice in lista:
        df.iloc[indice]

def nombresAgua():
    lista1=df[df['Type 1']=='Water'].index.tolist()
    lista2=df[df['Type 2']=='Water'].index.tolist()
    lista=lista1+lista2
    for indice in lista:
        df.iloc[indice]





