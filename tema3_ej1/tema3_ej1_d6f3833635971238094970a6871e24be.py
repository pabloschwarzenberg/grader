# completa el código de la función
def suma_divisores(a):
    counter = 0
    for i in range(1 , a):
        if a % i == 0:
            counter += i
    if counter == 1:
        return counter , True
        
    return counter , False
           