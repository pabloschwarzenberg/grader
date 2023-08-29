# completa el código de la función
def amigos(n):
    contador = 0
    for i in range(1, n+1):
        if n % i == 0:
            contador +=1
            
a = input("ingrese un numero: ")
b = input("ingrese un numero: ")

    if amigos(a) == amigos(b):
        return True
    else:
        return False
           