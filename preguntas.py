"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    data=open("./data.csv","r")
    counter=0
    for row in data:
        columa1=row.split(',')[0]
        number_specific=columa1.split("\t")[1]
        number=int(number_specific)
        counter+=number
    return counter

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    data=open("./data.csv","r")
    list_letter={}
    tuplas=[]
    for row in data:
        columa1=row.split(',')[0]
        letter_specific=columa1.split("\t")[0]
        if letter_specific in list_letter:
            list_letter[letter_specific]+=1
        else:
            list_letter[letter_specific]=1
    
    for key,value in list_letter.items():
        tuplas.append((key,value))
    tuplas.sort()
    return tuplas

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    data=open("./data.csv","r")
    letter_count={
        'A':0,
        'B':0,
        'C':0,
        'D':0,
        'E':0
    }
    list_letter_count=[]
    for row in data:
        columa1=row.split(',')[0]
        letter_specific=columa1.split("\t")[0]
        amount_for_letter=int(columa1.split("\t")[1])
        letter_count[letter_specific]+=amount_for_letter
    
    for key,value in letter_count.items():
        list_letter_count.append((key,value))
    
    return list_letter_count

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    data=open("./data.csv","r")
    month_count={}
    list_month_count=[]
    for row in data:
        columa1=row.split(',')[0]
        date=columa1.split('\t')[2]
        month=date.split('-')[1]
        if month in month_count:
            month_count[month]+=1
        else:
            month_count[month]=1
    
    for key,value in month_count.items():
        list_month_count.append((key,value))
    list_month_count.sort()
    return list_month_count

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    data=open("./data.csv","r")
    list_letter=[        
        {"letter":"A","max_value":None,"min_value":None},
        {"letter":"B","max_value":None,"min_value":None},
        {"letter":"C","max_value":None,"min_value":None},
        {"letter":"D","max_value":None,"min_value":None},
        {"letter":"E","max_value":None,"min_value":None}
      ]
    def max_min(letr,value):
        for i in list_letter:
            if letr == i["letter"]:
                if i["min_value"] is None:
                    i["min_value"]=value
                else:
                    if value<i["min_value"]:
                        i["min_value"]=value

                if i["max_value"] is None:
                    i["max_value"]=value
                else:
                    if value>i["max_value"]:
                        i["max_value"]=value
                break    
    for row in data:
        columa1=row.split(',')[0]
        letter_specific=columa1.split("\t")[0]
        count=int(columa1.split("\t")[1]) 
        max_min(letter_specific,count)
    sort_list=[]
    for data in list_letter:
        sort_list.append((data["letter"],data["max_value"],data["min_value"]))
    return sort_list

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    keys_data={}
    def max_min(list):
        new_list=list
        for row in new_list:
            new_row=row.split(':')
            clave=new_row[0]
            valor=int(new_row[1])

            if clave not in keys_data:
                keys_data[clave]={'key':clave,'min_value':valor,'max_value':valor}
            else:
                if valor<keys_data[clave]['min_value']:
                    keys_data[clave]['min_value']=valor
                if valor>keys_data[clave]['max_value']:
                    keys_data[clave]['max_value']=valor

    data=open("./data.csv","r")

    for row in data:
        keys=row.split('\t')[4]
        key=keys.split(',')
        list_keys=key[0:len(key)-1]
        last_key=key[len(key)-1].split('\n')[0]
        list_keys.append(last_key)
        max_min(list_keys)
    
    sorted_dict = dict(sorted(keys_data.items()))
    list_tuples=[]
    for i in sorted_dict.values():
        list_tuples.append((i['key'],i['min_value'],i['max_value']))
    return list_tuples

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    
    data=open("./data.csv","r")
    response={}

    for row in data:
        column1=row.split(',')[0]
        column1=column1.split('\t')

        ltr_csv=column1[0]
        number_csv=column1[1]

        if number_csv not in response:
            response[number_csv]={'key':number_csv,'list':[ltr_csv]}
        else:
            response[number_csv]['list'].append(ltr_csv)

    sorted_dict = dict(sorted(response.items()))
    list_sort=[]
    for i in sorted_dict:
        list_sort.append((int(sorted_dict[i]['key']),sorted_dict[i]['list']))
    return list_sort

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    data=open("./data.csv","r")
    response={}

    for row in data:
        column1=row.split(',')[0]
        column1=column1.split('\t')

        ltr_csv=column1[0]
        number_csv=column1[1]

        if number_csv not in response:
            response[number_csv]={'key':number_csv,'list':[ltr_csv]}
        else:
            if ltr_csv not in response[number_csv]['list']:
                response[number_csv]['list'].append(ltr_csv)
                response[number_csv]['list'].sort()

    sorted_dict = dict(sorted(response.items()))
    list_sort=[]
    for i in sorted_dict:
        list_sort.append((int(sorted_dict[i]['key']),sorted_dict[i]['list']))
    return list_sort

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    import re
    data=open("./data.csv","r")
    registros_claves={}

    for row in data:
        column=row.split(',')
        registros=[]
        for string_column in column:
            x=re.findall('[a-z][a-z][a-z]:[0-999]',string_column)
            if len(x)>0:
                registros.append(x[0])
        for cadena in registros:
            valores=cadena.split(':')
            clave=valores[0]

            if clave not in registros_claves:
                registros_claves[clave]=1
            else:
                registros_claves[clave]+=1
    sorted_dict = dict(sorted(registros_claves.items()))
    return sorted_dict


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    import re
    data=open("./data.csv","r")
    registros_clave=[]

    for row in data:
        column=row.split(',')
        column4=[]
        column5=[]
        clave=''

        for string_column in column:

            ltr_upper=re.findall('[A-Z]',string_column)
            if len(ltr_upper)>0:
                ltr_upper=ltr_upper[0]
                clave+=ltr_upper

            ltr=re.findall(r'\b[a-z]\b',string_column)
            if len(ltr)>0:
                new_ltr=ltr[0]
                column4.append(new_ltr)

            x=re.findall(r":[0-9]+",string_column)
            if len(x)>0:
                new_x=int(x[0].replace(':',''))
                column5.append(new_x)

        registros_clave.append((clave,len(column4),len(column5)))
        print(column4)
        print(column5)
        print(clave)
        break
pregunta_10() 


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    import re
    data=open("./data.csv","r")
    registros_clave={}

    for row in data:
        column=row.split(',')
        registros=0
        clave=''

        for string_column in column:

            ltr=re.findall('[A-Z]',string_column)
            if len(ltr)>0:
                new_ltr=ltr[0]
                clave+=new_ltr

            x=re.findall(r":[0-9]+",string_column)
            if len(x)>0:
                new_x=int(x[0].replace(':',''))
                registros+=new_x     

        if clave not in registros_clave:
            registros_clave[clave]=registros
        else:
            registros_clave[clave]+=registros

    sorted_dict = dict(sorted(registros_clave.items()))
    return sorted_dict
    
