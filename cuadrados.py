def cuadrados(lista):
    if lista==[]:
        return []
    return [x*x for x in lista]

print(cuadrados(list(range(1,11))))
