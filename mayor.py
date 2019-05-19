def mayor(lista):
    if len(lista) == 1:
        return lista[0]
    elif mayor(lista[1:]) > lista[0]:
        return mayor(lista[1:])  
    else:
        return lista[0]
        
print(mayor([27,24,56,93,21,237,46,74,125]))
