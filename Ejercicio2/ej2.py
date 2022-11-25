import csv
import pandas as pd

df = pd.read_csv("pokemon.csv")

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

def nombresFuego():
    lista1=df[df['Type 1']=='Fire'].index.tolist()
    lista2=df[df['Type 2']=='Fire'].index.tolist()
    lista=lista1+lista2
    for indice in lista:
        df.iloc[indice]

def nombresPlanta():
    lista1=df[df['Type 1']=='Grass'].index.tolist()
    lista2=df[df['Type 2']=='Grass'].index.tolist()
    lista=lista1+lista2
    for indice in lista:
        df.iloc[indice]

def nombresElec():
    lista1=df[df['Type 1']=='Electric'].index.tolist()
    lista2=df[df['Type 2']=='Electric'].index.tolist()
    lista=lista1+lista2
    for indice in lista:
        df.iloc[indice]

def ordenascendente():
    return df.iloc[::-1]






