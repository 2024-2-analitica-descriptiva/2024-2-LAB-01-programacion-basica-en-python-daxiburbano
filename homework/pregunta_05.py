"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open('files/input/data.csv', 'r') as file:
        data= file.readlines()
        #otra forma: 
        #data = [i.split("\t")[:2] for i in file.readlines()]

    # min_max = [
    #     (
    #         key,
    #         max(int(value) for k, value in data if k == key),
    #         min(int(value) for k, value in data if k == key),
    #     )
    #     for key in set(k for k, _ in data)
    # ]
    # return sorted(min_max)

        letter=[(x.split("\t")[0], int(x.split("\t")[1])) for x in data]
        listletter=set([x.split("\t")[0] for x in data])

        minmax=[]
        for i in listletter:
            tmp=list(filter(lambda x: x[0]==i, letter))
            minmax.append((i, max(tmp)[1], min(tmp)[1]))
        return sorted(minmax)

print(pregunta_05())