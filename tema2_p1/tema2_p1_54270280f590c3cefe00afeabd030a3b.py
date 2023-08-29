# por favor escribe aquí tu función
def es_primo(numero):
    total = 0

    for i in range(1, numero+1):
        if numero % i == 0:
            total = total + 1
        
    if total == 2:
        return True
    else:
        return False
numero = 123

   

 
           