def lista_ordenada(lista):

    if lista != [] and len(lista)>1:
     return (lista[0]<=lista[1]) and lista_ordenada(lista[1:])
    return True

print(lista_ordenada(['a','b','c','d']))

#Santiago Gómez Almeyda 20161020503
