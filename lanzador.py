import sys

sys.path.insert(0,"/Users/smite/Documents/GitHub/EvaluacionT4/Ejercicio1/ej1")
sys.path.insert(0,"/Users/smite/Documents/GitHub/EvaluacionT4/Ejercicio2/ej2")
sys.path.insert(0,"/Users/smite/Documents/GitHub/EvaluacionT4/Ejercicio3/ej3")

from Ejercicio1 import ej1
from Ejercicio2 import *
from Ejercicio3 import ej3

def exe():
    ejercicio=input("Introduce el numero del ejercicio que quieras lanzar:")

    if ejercicio==1:
        mensaje = input("Introduce un mensaje que contenga: A, 0, 1, 3, F, M, T")

        encriptado=ej1.encriptado(mensaje)
        print(f"El mensaje codificado es {encriptado}")
        desencriptado=ej1.DesencriptaHuff(encriptado)
        print(f"El mensaje decodificado es {desencriptado}")

    if ejercicio==2:
        


