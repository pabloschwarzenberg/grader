# por favor escribe aquí tu función
# Para ser primo el numero tiene que ser:
# divisible por 1 y divisible por el mismo

def es_primo(x):
    if x<2:
        return False
    elif x==2:
        return True
    else:
        for n in range(2,x):
            if x%n == 0:
                return False
        if(n == x-1):
            return True


