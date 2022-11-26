import sys

sys.path.insert(0,"/Users/smite/Documents/GitHub/EvaluacionT4/Ejercicio1/ej1")
sys.path.insert(0,"/Users/smite/Documents/GitHub/EvaluacionT4/Ejercicio2/ej2")
sys.path.insert(0,"/Users/smite/Documents/GitHub/EvaluacionT4/Ejercicio3/ej3")

from Ejercicio1 import ej1
from Ejercicio2 import ej2
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
        ej2.nombresAgua()
        ej2.nombresElec()
        ej2.nombresFuego()
        ej2.nombresPlanta()
        ej2.ordenascendente()
        ej2.debilesJolteon()
        ej2.debilesLycanroc()
        ej2.debilesTyrantrum()
        ej2.mostrarTipos()

    if ejercicio==3:

        maravillas=[{'Nombre': 'Gran Muralla China', 'Pais': 'China', 'Tipo': 'ARQUITECTURA'}, {'Nombre': 'Coliseo de Roma' , 'Pais': 'Italia' , 'Tipo': 'ARQUITECTURA'},
            {'Nombre': 'Ciudad de Petra', 'Pais': 'Jordania ' , 'Tipo': 'ARQUITECTURA'}, {'Nombre': 'Bahía de Ha Long', 'Pais': 'Vietnam' , 'Tipo': 'NATURAL'},
            {'Nombre': 'Isla Jeju', 'Pais': 'Corea Sur' , 'Tipo': 'NATURAL'}, {'Nombre': 'Machu Picchu', 'Pais': 'Peru' , 'Tipo': 'ARQUITECTURA'},
            {'Nombre': 'Taj Mahal', 'Pais': 'India', 'Tipo':'ARQUITECTURA'}]

        dist = [['Gran Muralla China', 'Coliseo de Roma', 7462], ['Coliseo de Roma','Machu Picchu', 10708], ['Gran Muralla China', 'Ciudad de Petra', 6318],
        ['Gran Muralla China', 'Machu Picchu', 16888], ['Gran Muralla China', 'Taj Mahal', 7470], ['Ciudad de Petra','Taj Mahal', 4296],
        ['Coliseo de Roma','Ciudad de Petra', 3673], ['Bahía de Ha Long', 'Isla Jeju', 2362 ],['Machu Picchu', 'Taj Mahal', 17041],
        ['Coliseo de Roma','Taj Mahal', 6640], ['Ciudad de Petra', 'Machu Picchu',  12441]]

        ej3.paisambasmaravillas(maravillas)
        ej3.paismismasmaravillasnatu(maravillas)
        ej3.paismismasmaravillasarq(maravillas)

    else:
        print('Número de ejercicio incorrecto.(dDebe ser 1,2 o 3)')



