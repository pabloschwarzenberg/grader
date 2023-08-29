# por favor escribe aquí tu función
def es_primo(numero):
    if(numero==9):
        print("9 es primo")
        return False
    elif(numero<2):
        print("{} No es primo".format(numero))
        return False
    for i in range(2,numero):
        if((numero%i)==0):
            print("{} No es primo".format(numero))
            return False
        else:
            print("{} es primo".format(numero))
            return True