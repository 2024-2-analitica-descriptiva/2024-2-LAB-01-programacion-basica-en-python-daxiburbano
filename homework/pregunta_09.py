"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    with open('files/input/data.csv', 'r') as file:
        data= file.readlines()
        l1= [(x.split("\t")[4].replace('\n','').split(",")) for x in data]

        #1 Aplanar l1 para procesar todos los elementos (clave:valor)
        l2= [item for sublist in l1 for item in sublist]

        #2 Dividir clave:valor (valor es _ quiere decir que no se requiere)
        data = [key for key, _ in (item.split(":") for item in l2)]

        #otra forma de evitar #1 y #2
        #import itertools
        #data = [x.split(":")[0] for x in list(itertools.chain(*l1))]
        
        conteo=sorted([(x, data.count(x)) for x in set(data)])
        return dict(conteo)

print(pregunta_09())