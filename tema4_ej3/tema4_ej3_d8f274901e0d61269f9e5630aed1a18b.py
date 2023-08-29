def jerigonzo(string):
    #multiplicacion de variable de entrada
    thestring = string
    #Lista
    lista=[]
    repeticiones = 0
    largo = len(thestring)
    distancia = len(thestring)
    long = int(largo) - 1
    paseastring = str(thestring)
    #Bucle principal
    while int(largo) > repeticiones:
        posicion = paseastring[long]
        ciclos = posicion
        letra = ciclos
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            thestring = posicion+"p"+letra
            lista.append(thestring)
            repeticiones = repeticiones + 1
            long = long - 1
        else:
            lista.append(posicion)
            repeticiones = repeticiones + 1
            long = long - 1
    #solucion desesperada road to los puntitos
    distanciafinal = int(distancia)-1
    if distanciafinal == 20:
        string = lista[distanciafinal]+lista[distanciafinal - 1]+lista[distanciafinal - 2]+lista[distanciafinal - 3]+lista[distanciafinal - 4]+lista[distanciafinal - 5]+lista[distanciafinal - 6]+lista[distanciafinal - 7]+lista[distanciafinal - 8]+lista[distanciafinal - 9]+lista[distanciafinal - 10]+lista[distanciafinal - 11]+lista[distanciafinal - 12]+lista[distanciafinal - 13]+lista[distanciafinal - 14]+lista[distanciafinal - 15]+lista[distanciafinal - 16]+lista[distanciafinal - 17]+lista[distanciafinal - 18]+lista[distanciafinal - 19]+lista[distanciafinal - 20]
    if distanciafinal == 19:
        string = lista[distanciafinal]+lista[distanciafinal - 1]+lista[distanciafinal - 2]+lista[distanciafinal - 3]+lista[distanciafinal - 4]+lista[distanciafinal - 5]+lista[distanciafinal - 6]+lista[distanciafinal - 7]+lista[distanciafinal - 8]+lista[distanciafinal - 9]+lista[distanciafinal - 10]+lista[distanciafinal - 11]+lista[distanciafinal - 12]+lista[distanciafinal - 13]+lista[distanciafinal - 14]+lista[distanciafinal - 15]+lista[distanciafinal - 16]+lista[distanciafinal - 17]+lista[distanciafinal - 18]+lista[distanciafinal - 19]
    if distanciafinal == 18:
        string = lista[distanciafinal]+lista[distanciafinal - 1]+lista[distanciafinal - 2]+lista[distanciafinal - 3]+lista[distanciafinal - 4]+lista[distanciafinal - 5]+lista[distanciafinal - 6]+lista[distanciafinal - 7]+lista[distanciafinal - 8]+lista[distanciafinal - 9]+lista[distanciafinal - 10]+lista[distanciafinal - 11]+lista[distanciafinal - 12]+lista[distanciafinal - 13]+lista[distanciafinal - 14]+lista[distanciafinal - 15]+lista[distanciafinal - 16]+lista[distanciafinal - 17]+lista[distanciafinal - 18]
    if distanciafinal == 17:
        string = lista[distanciafinal]+lista[distanciafinal - 1]+lista[distanciafinal - 2]+lista[distanciafinal - 3]+lista[distanciafinal - 4]+lista[distanciafinal - 5]+lista[distanciafinal - 6]+lista[distanciafinal - 7]+lista[distanciafinal - 8]+lista[distanciafinal - 9]+lista[distanciafinal - 10]+lista[distanciafinal - 11]+lista[distanciafinal - 12]+lista[distanciafinal - 13]+lista[distanciafinal - 14]+lista[distanciafinal - 15]+lista[distanciafinal - 16]+lista[distanciafinal - 17]
    if distanciafinal == 16:
        string = lista[distanciafinal]+lista[distanciafinal - 1]+lista[distanciafinal - 2]+lista[distanciafinal - 3]+lista[distanciafinal - 4]+lista[distanciafinal - 5]+lista[distanciafinal - 6]+lista[distanciafinal - 7]+lista[distanciafinal - 8]+lista[distanciafinal - 9]+lista[distanciafinal - 10]+lista[distanciafinal - 11]+lista[distanciafinal - 12]+lista[distanciafinal - 13]+lista[distanciafinal - 14]+lista[distanciafinal - 15]+lista[distanciafinal - 16]
    if distanciafinal == 15:
        string = lista[distanciafinal]+lista[distanciafinal - 1]+lista[distanciafinal - 2]+lista[distanciafinal - 3]+lista[distanciafinal - 4]+lista[distanciafinal - 5]+lista[distanciafinal - 6]+lista[distanciafinal - 7]+lista[distanciafinal - 8]+lista[distanciafinal - 9]+lista[distanciafinal - 10]+lista[distanciafinal - 11]+lista[distanciafinal - 12]+lista[distanciafinal - 13]+lista[distanciafinal - 14]+lista[distanciafinal - 15]
    if distanciafinal == 14:
        string = lista[distanciafinal]+lista[distanciafinal - 1]+lista[distanciafinal - 2]+lista[distanciafinal - 3]+lista[distanciafinal - 4]+lista[distanciafinal - 5]+lista[distanciafinal - 6]+lista[distanciafinal - 7]+lista[distanciafinal - 8]+lista[distanciafinal - 9]+lista[distanciafinal - 10]+lista[distanciafinal - 11]+lista[distanciafinal - 12]+lista[distanciafinal - 13]+lista[distanciafinal - 14]
    if distanciafinal == 13:
        string = lista[distanciafinal]+lista[distanciafinal - 1]+lista[distanciafinal - 2]+lista[distanciafinal - 3]+lista[distanciafinal - 4]+lista[distanciafinal - 5]+lista[distanciafinal - 6]+lista[distanciafinal - 7]+lista[distanciafinal - 8]+lista[distanciafinal - 9]+lista[distanciafinal - 10]+lista[distanciafinal - 11]+lista[distanciafinal - 12]+lista[distanciafinal - 13]
    if distanciafinal == 12:
        string = lista[distanciafinal]+lista[distanciafinal - 1]+lista[distanciafinal - 2]+lista[distanciafinal - 3]+lista[distanciafinal - 4]+lista[distanciafinal - 5]+lista[distanciafinal - 6]+lista[distanciafinal - 7]+lista[distanciafinal - 8]+lista[distanciafinal - 9]+lista[distanciafinal - 10]+lista[distanciafinal - 11]+lista[distanciafinal - 12]
    if distanciafinal == 11:
        string = lista[distanciafinal]+lista[distanciafinal - 1]+lista[distanciafinal - 2]+lista[distanciafinal - 3]+lista[distanciafinal - 4]+lista[distanciafinal - 5]+lista[distanciafinal - 6]+lista[distanciafinal - 7]+lista[distanciafinal - 8]+lista[distanciafinal - 9]+lista[distanciafinal - 10]+lista[distanciafinal - 11]
    if distanciafinal == 10:
        string = lista[distanciafinal]+lista[distanciafinal - 1]+lista[distanciafinal - 2]+lista[distanciafinal - 3]+lista[distanciafinal - 4]+lista[distanciafinal - 5]+lista[distanciafinal - 6]+lista[distanciafinal - 7]+lista[distanciafinal - 8]+lista[distanciafinal - 9]+lista[distanciafinal - 10]
    if distanciafinal == 9:
        string = lista[distanciafinal]+lista[distanciafinal - 1]+lista[distanciafinal - 2]+lista[distanciafinal - 3]+lista[distanciafinal - 4]+lista[distanciafinal - 5]+lista[distanciafinal - 6]+lista[distanciafinal - 7]+lista[distanciafinal - 8]+lista[distanciafinal - 9]
    if distanciafinal == 8:
        string = lista[distanciafinal]+lista[distanciafinal - 1]+lista[distanciafinal - 2]+lista[distanciafinal - 3]+lista[distanciafinal - 4]+lista[distanciafinal - 5]+lista[distanciafinal - 6]+lista[distanciafinal - 7]+lista[distanciafinal - 8]
    if distanciafinal == 7:
        string = lista[distanciafinal]+lista[distanciafinal - 1]+lista[distanciafinal - 2]+lista[distanciafinal - 3]+lista[distanciafinal - 4]+lista[distanciafinal - 5]+lista[distanciafinal - 6]+lista[distanciafinal - 7]
    if distanciafinal == 6:
        string = lista[distanciafinal]+lista[distanciafinal - 1]+lista[distanciafinal - 2]+lista[distanciafinal - 3]+lista[distanciafinal - 4]+lista[distanciafinal - 5]+lista[distanciafinal - 6]
    if distanciafinal == 5:
        string = lista[distanciafinal]+lista[distanciafinal - 1]+lista[distanciafinal - 2]+lista[distanciafinal - 3]+lista[distanciafinal - 4]+lista[distanciafinal - 5]
    if distanciafinal == 4:
        string = lista[distanciafinal]+lista[distanciafinal - 1]+lista[distanciafinal - 2]+lista[distanciafinal - 3]+lista[distanciafinal - 4]
    if distanciafinal == 3:
        string = lista[distanciafinal]+lista[distanciafinal - 1]+lista[distanciafinal - 2]+lista[distanciafinal - 3]
    if distanciafinal == 2:
        string = lista[distanciafinal]+lista[distanciafinal - 1]+lista[distanciafinal - 2]
    if distanciafinal == 1:
        string = lista[distanciafinal]+lista[distanciafinal - 1]
    return string

if __name__ == "__main__":
    pass
         