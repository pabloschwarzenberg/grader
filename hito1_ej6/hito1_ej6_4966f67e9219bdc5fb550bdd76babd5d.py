lista = []
lista.append(int(input("ingrese un valor: ")))
lista.append(int(input("ingrese un valor: ")))
lista.append(int(input("ingrese un valor: ")))
auxiliar = None
for i in range(len(lista)):
    for cualquierwea in range(2):
        if not (lista[cualquierwea] < lista[cualquierwea+1]):
            auxiliar = lista[cualquierwea]
            lista[cualquierwea] = lista[cualquierwea+1]
            lista[cualquierwea+1] = auxiliar

        
print("%d,%d,%d"%(lista[0],lista[1],lista[2]))