#Garcia Ramos Ezequiel 215465492
#Modulo 1 Analizador Mini Analizador Lexico
#Fecha: 21/08/2021
#Seminario de traductores de lenguaje 2

import re # Biblioteca de Expresiones Regulares
ID = re.compile(r'[a-zA-Z]+[\w]*') #Se crea una forumla patron para ID
Real = re.compile(r'[\d]+\.[\d]+')

if __name__ == '__main__':
    entrada = 'num1'
    matches = ID.match(entrada)
    if matches:
        print(matches.group())
    else:
        print('No coincide')

    entrada = '12.3'
    matches = Real.match(entrada)
    if matches:
        print(matches.group())
    else:
        print('No coincide')