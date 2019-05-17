def sumar(lista):
    if lista == []:
        return 0
   
    return lista[0]+ sumar(lista[1:])
    
print(sumar([5,4,7,8]))

#Santiago Gómez Almeyda
