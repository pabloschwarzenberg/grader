# por favor escribe aquí tu función
def es_primo(num):
    if num == 1:
        return False
    for n in range(2, num):
        if num%n == 0: 
            return False
    if num != 1:   
        return True


 