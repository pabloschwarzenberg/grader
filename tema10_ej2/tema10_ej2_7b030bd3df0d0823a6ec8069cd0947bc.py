def levenshtein(palabra1,palabra2):
    lista = list(palabra1)
    lista2 = list(palabra2)
    lista3 = []
    igual = []
    lista_1 = ["x,y"]
    if(len(lista) > len(lista2)):
        largo_max = lista
        largo_min = lista2
    elif(len(lista) < len(lista2)):
        largo_max = lista2
        largo_min = lista
    elif(len(lista) == len(lista2)):
        largo_max = lista
        largo_min = lista2
    largo = len(largo_max) - 2
    largo2 = len(largo_max) -1
    if(largo == len(largo_min)):
        mayor_1 = 1
    elif(4 > len(lista3)):
        mayor_1 = 1
    else:
        mayor_1 = 0
    for i in range(len(largo_min)):
        if(largo_max[i] != largo_min[i]):
            lista3.append(lista[i])
    if(len(largo_max) > len(largo_min) and 3 >= len(lista3) and largo2 == len(largo_min)):
        respuesta = "IB"
        return respuesta
    if(igual == lista3):
        respuesta = "0D"
        return respuesta
    if(len(largo_max) == len(largo_min) and 1 == len(lista3)):
        respuesta = "1S"
        return respuesta
    if(mayor_1 == 1):
        respuesta = "+1"
        return respuesta
    print("lista3",lista3)    
if __name__=="__main__":
    palabra1 = input("Ingrese una palabra")
    palabra2 = input("Ingrese una palabra")
    palabra3 = levenshtein(palabra1,palabra2)       