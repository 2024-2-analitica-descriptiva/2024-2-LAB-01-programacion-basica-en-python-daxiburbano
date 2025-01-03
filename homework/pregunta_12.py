"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    with open('files/input/data.csv', 'r') as file:
        data= file.readlines()
        data1=[(i.split("\t")[0] , i.split("\t")[4].replace("\n", "").split(",")) for i in data] # [('E', ['jjj:12', 'bbb:3', 'ddd:9', 'ggg:8', 'hhh:2']), ('A', ['ccc:2', 'ddd:0', 'aaa:3', 'hhh:9'])
        data2= [(key, int(item.split(":")[1])) for key, values in data1 for item in values ]      #[('E', 12), ('E', 3), ('E', 9), ('E', 8), ('E', 2), ('A', 2), ('A', 0), ('A', 3), ('A', 9)

        # Obtener valores unicos de las letras
        listletter=set([x.split("\t")[0] for x in data])

        agrupa=[]
        for i in listletter:
            tmp=filter(lambda x: x[0]==i, data2)
            agrupa.append((i, sum([x[1] for x in tmp])))
        return dict(sorted(agrupa))
 
print(pregunta_12())