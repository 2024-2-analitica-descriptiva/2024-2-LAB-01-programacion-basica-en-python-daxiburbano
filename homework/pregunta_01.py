"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    # leer el archivo

    with open('files/input/data.csv', 'r') as file:
        data= file.readlines()
        data=[int(x.split("\t")[1]) for x in data]
        return sum(data)

print(pregunta_01())