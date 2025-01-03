"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    with open('files/input/data.csv', 'r') as file:
        data= file.readlines()
        l1= [(x.split("\t")[4].replace('\n','').split(",")) for x in data]

        # Aplanar l1 para procesar todos los elementos (clave:valor)
        l2= [item for sublist in l1 for item in sublist]

        # Dividir clave:valor y convertir valor a entero
        result = [[key, int(value)] for key, value in (item.split(":") for item in l2)]
        #print(result)
        
        # Obtener valores unicos de las letras
        listletter=set(item[0] for item in result)

        minmax=[]
        for i in listletter:
            tmp=list(filter(lambda x: x[0]==i, result))
            minmax.append((i, min(tmp)[1], max(tmp)[1]))
        return sorted(minmax)

print(pregunta_06())