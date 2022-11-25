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

def debilesJolteon():
    lista1=df[df['Type 1']=='Water'].index.tolist()
    lista2=df[df['Type 1']=='Fliying'].index.tolist()
    lista5=df[df['Type 2']=='Water'].index.tolist()
    lista6=df[df['Type 2']=='Fliying'].index.tolist()
    lista3=df[df['Type 1']=='Ground'].index.tolist()
    lista4=df[df['Type 2']=='Ground'].index.tolist()
    lista=lista1+lista2-lista3-lista4+lista5+lista6
    for indice in lista:
        df.iloc[indice]

def debilesLycanroc():
    lista1=df[df['Type 1']=='Fire'].index.tolist()
    lista2=df[df['Type 1']=='Fliying'].index.tolist()
    lista3=df[df['Type 1']=='Bug'].index.tolist()
    lista4=df[df['Type 1']=='Ice'].index.tolist()
    lista5=df[df['Type 2']=='Fire'].index.tolist()
    lista6=df[df['Type 2']=='Fliying'].index.tolist()
    lista7=df[df['Type 2']=='Bug'].index.tolist()
    lista8=df[df['Type 2']=='Ice'].index.tolist()
    lista=lista1+lista2+lista3+lista4+lista5+lista6+lista7+lista8
    for indice in lista:
        df.iloc[indice]

def debilesTyrantrum():
    lista1=df[df['Type 1']=='Fire'].index.tolist()
    lista2=df[df['Type 1']=='Fliying'].index.tolist()
    lista3=df[df['Type 1']=='Bug'].index.tolist()
    lista4=df[df['Type 1']=='Ice'].index.tolist()
    lista5=df[df['Type 2']=='Fire'].index.tolist()
    lista6=df[df['Type 2']=='Fliying'].index.tolist()
    lista7=df[df['Type 2']=='Bug'].index.tolist()
    lista8=df[df['Type 2']=='Ice'].index.tolist()
    lista9=df[df['Type 1']=='Dragon'].index.tolist()
    lista10=df[df['Type 1']=='Fairy'].index.tolist()
    lista11=df[df['Type 2']=='Fairy'].index.tolist()
    lista=lista1+lista2+lista3+lista4+lista5+lista6+lista7+lista8+lista9-lista10-lista11
    for indice in lista:
        df.iloc[indice]

def mostrarTipos():
    tipos=[]
    for column in df.columns['Type 1']:
        if column not in tipos:
            tipos.append(column)
    return tipos

def mostrarPokeTipo(tipo):
    lista1=df[df['Type 1']==str(tipo)].index.tolist()
    lista2=df[df['Type 1']==str(tipo)].index.tolist()
    lista=lista1+lista2
    for indice in lista:
        df.iloc[indice]








