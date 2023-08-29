# completa el código de la función
def suma_divisores(a):
    numero = a 
    contador = 0
    for i in range(1,numero):
        if (numero % i) == 0:
            contador += 1
    if contador == 1 and numero != 1:
        print(contador,",")
        return True
    if contador >= 2:
        return False
    if numero == 1:
        return False
           