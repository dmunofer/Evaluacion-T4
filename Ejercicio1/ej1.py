
class Nodos():
    def __init__(self,frecuencia,simbolo,left=None,right=None):
        self.frecuencia=frecuencia
        self.simbolo=simbolo
        self.left=left
        self.right=right
        self.code=''

def encriptado(datos,coding):
    encriptado=[]
    for dato in datos:
        encriptado.append(coding[dato])
    cadena=  ''.join([str(item) for item in encriptado])
    return cadena

def Huffman(datos):
    simbolosconfrecs={"A":"00", "1":"01", "3":"100", "0":"1010", "M":"1011", "T":"110", "F":"111"}
    simbolos= ["A", "F", "1", "3", "0", "M", "T"]
    frecuencias= [0.2, 0.17, 0.13, 0.21, 0.05, 0.09, 0.15]
    nodos=[]
    for simbolo in simbolos:
        nodos.append(Nodos(simbolosconfrecs.get(simbolo), simbolo))