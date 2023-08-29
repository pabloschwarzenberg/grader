# por favor escribe aquí tu función
def es_primo(numero):
    if numero == 1:
        return False
    else:
        count = 0

        for i in range(1,numero + 1):
            
            if numero % i == 0:
                print(count)
                count= count + 1
        if count==2:
            return True
        else:
            return False
