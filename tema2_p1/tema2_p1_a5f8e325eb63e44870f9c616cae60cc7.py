# por favor escribe aquí tu función
def es_primo(num,n=2):
    if num == 0 or num == 1 or num == 4:
        return False
    if(n >= num):
        print("es primo")
        return True
    elif (num % n !=0):
        return es_primo(num, n+1)
    else:
        print("no es primo")
        return False
