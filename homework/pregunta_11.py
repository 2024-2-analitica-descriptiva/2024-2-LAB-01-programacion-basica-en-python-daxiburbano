"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    with open('files/input/data.csv', 'r') as file:
        data= file.readlines()
        data= [(int(x.split("\t")[1]), x.split("\t")[3]) for x in data] #entrega [(1, 'b,g,f'), (2, 'a,f,c')...]
        data=[(key, value.split(',')) for key, value in data] #[(1, ['b', 'g', 'f']), (2, ['a', 'f', 'c'])...]
        
        # Obtener valores unicos de las letras
        listletter= set(letter for _, letters in data for letter in letters)

        agrupa=[]
        for i in listletter:
            tmp=filter(lambda x: i in x[1], data)
            agrupa.append((i, sum([x[0] for x in tmp])))
        return dict(sorted(agrupa))

print(pregunta_11())