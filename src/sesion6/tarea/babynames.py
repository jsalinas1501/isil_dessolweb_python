#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0


import sys
import csv
import re

"""
Baby Names
==========

Defina la funcion extract_names() de abajo y modique main()
para que la invoque.

Asi es como los archivos html lucen babyxxxx.html

...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Hitos sugeridos para el desarrollo incremental::
 -Extraer el año e imprimirlo.
 -Extraer los nombres y rangos(ranks) e imprimirlos.
 -Obtener los nombres dentro de diccionarios e imprimirlos.
 -Armar la lista [año, "nombre rango(rank)", ...]
 -Corregir main() para usar la lista que retorne la funcion extract_names.
"""


def extract_names(filename):
    """
    Dado un nombre de archivo, devuelve una lista que comienza con
    el año como cadena seguido de las cadenas de "nombres rango" en orden
    alfabético.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    # +++tu codigo va aqui+++
    
    nombres=[]

    f=open("baby1990.html","rU")
    text=f.read()

    year=re.search(r'Popularity\sin\s(\d\d\d\d)', text)
    if not year:
        sys.stderr.write('Couldn\'t find the year!\r\n')
        sys.exit(1)
        
    year1=year.group(1)
    nombres.append(year1)

    tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', text)
    
    for rank_nombres in tuples:
        (rank, nino, nina) = rank_nombres
        if nino not in nombres:
            nombres.append(nino + " " + rank)
        if nina not in nombres:
            nombres.append(nina + " " + rank)

    sorted_nombres=sorted(nombres)
    
    return sorted_nombres


def main():
    # Se pasa una serie de archivos omitimos el argumento argv[0]
    # el cual nos trae el nombre del archivo.
    args = sys.argv[1:]

    if not args:
        print('usage: [--generaresumen] archivo [archivo ...]')
        sys.exit(1)

    # Observe que el flag generaresumen.
    summary = False
    if args[0] == '--generaresumen':
        summary = True
        del args[0]

    # +++tu codigo va aqui+++
    # Por cada archivo pasado como parametro imprimir el resultado.
    # En caso se pase el flag generaresumen, guardar en un archivo
    # con el mismo nombre pero la extension .resumen

    # Ejemplo:
    # $ python babynames.py baby1990.html baby1992.html
    # $ python babynames.py --generaresumen baby1990.html baby1992.html
    
    for filename in args:
        nombres=extract_names(filename)
        #print(nombres)
        text="\n".join(nombres)

        if summary:
            x=open(filename+".resumen","w")
            x.write(text+"\n")
            x.close()

        else:
            print(text)

if __name__ == '__main__':
    main()