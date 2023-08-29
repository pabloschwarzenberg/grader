# por favor escribe aquí tu función
def es_primo(numero):
    a = 0
    for i in range(1, numero+1):
        if numero % i == 0:
            a += 1
    if a == 2:
        print("el numero es primo")
    else:
        print("el numero no es primo")
        

      
 