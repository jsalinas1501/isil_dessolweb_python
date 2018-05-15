def principal():

    #EJERCICIO NUMERO 1:
    mylista = [2,5,8,12,16,21]

    suma=0
    for num in mylista:
        suma=suma+(num**2)

    print("El resultado del ejercicio 1 es: ", suma)

    #EJERCICIO NUMERO 2:
    texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do..."
    lista_texto=list(texto)

    #print(lista_texto)

    contador=0
    for letra in lista_texto:
        if(letra=='a'):
            contador=contador+1

    print(contador)


if __name__=='__main__':
    principal()