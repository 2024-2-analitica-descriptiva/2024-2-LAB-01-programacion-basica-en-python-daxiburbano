"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    with open('files/input/data.csv', 'r') as file:
        data= file.readlines()
        data=[x.split("\t")[0] for x in data]
        data=sorted([(x, data.count(x)) for x in set(data)])

        # si quiero contar todos los elementos que tengo en la lista de otra forma
        #from collections import Counter
        #data= sorted(list(Counter(data).items()))

        return data

print(pregunta_02())