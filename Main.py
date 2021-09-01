#Garcia Ramos Ezequiel 215465492
#Modulo 1 Analizador Mini Analizador Lexico
#Fecha: 21/08/2021
#Seminario de traductores de lenguaje 2
import Analizador_Lexico
fuente = []  # Lista Vacía de concatenacion

#Lectura del TXT
with open('programa.txt') as linea_de_entrada: #abrimos en modo lectura
    for fila in linea_de_entrada: #se lee cada fila del archivo
        fuente.extend(fila.split())  #Separamos las palabras y quitamos saltos de linea

fuente.append('$') #le agregamos el delimitador de finalizar

print('Analizador Lexico\n')
print('Elemento\t\t\tTipo')


for palabra in fuente:
    # Si la palabra coincide con los patrones, la imprime con su respectivo tipo. Si no coincide imprime None
    if Analizador_Lexico.ID.match(palabra):
        print(f'{palabra}\t\t\tIdentificador')
    elif Analizador_Lexico.Real.match(palabra):
        print(f'{palabra}\t\t\t\tReal')
    elif palabra == '$':
        print(f'{palabra}\t\t\tFinalizo la cadena')
    else:
        print(f'{palabra}\t\t\t\tError')
