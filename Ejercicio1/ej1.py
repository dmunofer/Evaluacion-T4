
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
    