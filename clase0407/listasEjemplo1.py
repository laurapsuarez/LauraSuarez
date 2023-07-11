def buscarElemen(lst,elem):
    for i in range(len(lst)):
        if lst[i] == elem:
            return i
    return -1 

def encontrarElemen(lst,elem):
    for e in lst:
        if e == elem:
            return True
    return False
    
miLista = []
miLista = list()

print(miLista,len(miLista))
miLista.append("Alirio")
print(miLista,len(miLista))

miLista.extend(["andree","carlos","cristian","diana"])
print(miLista,len(miLista))

miLista.pop()
print(miLista)

miLista.insert(2,"lilian")
print(miLista)


# RECORRIDO POR INDICE
for elemento in range(len(miLista)):
    print(miLista[elemento])
    
# RECORRIDO POR ELEMENTO
print("*-*")
for elem in miLista:
    print(elem)
    
    
# BUSCAR UN ELEMENTO SI ESTA DEVUELVE LA POSICION Y SINO DEVUELVE -1
pos = buscarElemen(miLista,"carlos")
print(pos)

# buscar un elemento en la lista devuelve true o false si esta o no estae
esta = encontrarElemen(miLista,"carlos")
print(esta)

