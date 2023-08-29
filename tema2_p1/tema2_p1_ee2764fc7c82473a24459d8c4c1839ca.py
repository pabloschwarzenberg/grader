# por favor escribe aquí tu función
def es_primo(n):
    if n==9:
        print("9 no es primo")
        return False
    elif n<2:
        print("{} no es primo".format(n))
        return False
    for i in range(2,n):
        if(n%i)==0:
            print("{} no es primo".format(n))
            return False
        else:
            print("{} es primo".format(n))
            return True