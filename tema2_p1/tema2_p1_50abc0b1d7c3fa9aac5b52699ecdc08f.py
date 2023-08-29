# por favor escribe aquí tu función
def es_primo(num):
    if num<=1:
        print("Error No es Primo")
        return False
    else:
        for i in range(2,num-1):
            if num%i==0:
                print("Error No es Primo")
                return False
    if num%1==0 and num%num==0:
        print("Si es Primo")
        return True