maravillas=[{'Nombre': 'Gran Muralla China', 'Pais': 'China', 'Tipo': 'ARQUITECTURA'}, {'Nombre': 'Coliseo de Roma' , 'Pais': 'Italia' , 'Tipo': 'ARQUITECTURA'},
            {'Nombre': 'Ciudad de Petra', 'Pais': 'Jordania ' , 'Tipo': 'ARQUITECTURA'}, {'Nombre': 'Bahía de Ha Long', 'Pais': 'Vietnam' , 'Tipo': 'NATURAL'},
            {'Nombre': 'Isla Jeju', 'Pais': 'Corea Sur' , 'Tipo': 'NATURAL'}, {'Nombre': 'Machu Picchu', 'Pais': 'Peru' , 'Tipo': 'ARQUITECTURA'},
            {'Nombre': 'Taj Mahal', 'Pais': 'India', 'Tipo':'ARQUITECTURA'}]

dist = [['Gran Muralla China', 'Coliseo de Roma', 7462], ['Coliseo de Roma','Machu Picchu', 10708], ['Gran Muralla China', 'Ciudad de Petra', 6318],
        ['Gran Muralla China', 'Machu Picchu', 16888], ['Gran Muralla China', 'Taj Mahal', 7470], ['Ciudad de Petra','Taj Mahal', 4296],
        ['Coliseo de Roma','Ciudad de Petra', 3673], ['Bahía de Ha Long', 'Isla Jeju', 2362 ],['Machu Picchu', 'Taj Mahal', 17041],
        ['Coliseo de Roma','Taj Mahal', 6640], ['Ciudad de Petra', 'Machu Picchu',  12441]]

def paisambasmaravillas(lista):
    paisesambas=[]
    for maravilla in lista:
        cont=0
        if lista[maravilla]['Tipo']=='ARQUITECTURA':
            cont+=1
        elif lista[maravilla]['Tipo']=='NATURAL':
            cont+=1
        elif cont==2:
            paisesambas.append(lista[maravilla]['Pais'])
        else:
            pass
    return paisesambas

def paismismasmaravillas(lista):
    paisesambasnatu=[]
    for maravilla in lista:
        cont=0
        if lista[maravilla]['Tipo']=='NATURAL':
            cont+=1
        elif lista[maravilla]['Tipo']=='NATURAL':
            cont+=1
        elif cont==2:
            paisesambasnatu.append(lista[maravilla]['Pais'])
        else:
            pass
    return paisesambasnatu

def paismismasmaravillas(lista):
    paisesambasarq=[]
    for maravilla in lista:
        cont=0
        if lista[maravilla]['Tipo']=='ARQUITECTURA':
            cont+=1
        elif lista[maravilla]['Tipo']=='ARQUITECTURA':
            cont+=1
        elif cont==2:
            paisesambasarq.append(lista[maravilla]['Pais'])
        else:
            pass
    return paisesambasarq