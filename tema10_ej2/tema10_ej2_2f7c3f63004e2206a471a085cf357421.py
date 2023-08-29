#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(pal1,pal2):
    if pal1 == pal2:
        return "0D"
    if len(pal1) < len(pal2):
        mayor = pal2
        menor = pal1
    else:
        mayor = pal1
        menor = pal2
    if len(pal1) == len(pal2):
        mayor = pal1
        menor = pal2

    listaMayor = []
    listaMenor = []
    for letras in mayor:
        listaMayor.append(letras)
    for letras in menor:
        listaMenor.append(letras)

    print(listaMayor, listaMenor)

    i = 0
    while i < len(listaMenor):
        num = mayor.find(listaMenor[i])
        print(num)
        listaMayor[num] = ""
        print(listaMayor)
        i += 1
    
    distancia = ""
    for letra in listaMayor:
        distancia += letra
        
    distancia = len(distancia)
    print(distancia)

    if distancia > 1:
        return "+1"
    elif distancia == 1 and len(mayor) - len(menor) == 1:
        return "IB"
    elif len(mayor) == len(menor) and distancia == 1:
        return "1S"




