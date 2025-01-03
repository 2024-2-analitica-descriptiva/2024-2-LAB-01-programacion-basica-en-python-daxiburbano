"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    with open('files/input/data.csv', 'r') as file:
        data= file.readlines()
        #otra forma: 
        #data = [i.split("\t")[:2] for i in file.readlines()]
        #acumulado = {
            #key: sum(int(value) for k, value in data if k == key)
            #for key in set(k for k, _ in data)
        #}
        #return sorted(list(acumulado.items()))

        letter=[(x.split("\t")[0], int(x.split("\t")[1])) for x in data]
        listletter=set([x.split("\t")[0] for x in data])

        suma=[]
        for i in listletter:
            tmp=list(filter(lambda x: x[0]==i, letter))
            suma.append((i, sum([x[1] for x in tmp])))
        return sorted(suma)

print(pregunta_03())