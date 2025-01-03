"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
    with open('files/input/data.csv', 'r') as file:
        data= file.readlines()
        data= [(int(x.split("\t")[1]), x.split("\t")[0]) for x in data]
        
        # Obtener valores unicos de los números
        listnumber=set(item[0] for item in data)
        agrupa=[]
        for i in listnumber:
            tmp=list(filter(lambda x: x[0]==i, data))
            agrupa.append((i, sorted(set([x[1] for x in tmp]))))
        return sorted(agrupa)

print(pregunta_08())