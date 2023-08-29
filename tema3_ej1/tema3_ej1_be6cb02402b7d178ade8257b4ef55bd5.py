# completa el código de la función
def suma_divisores(numero):
    num = 0
    for i in range(1, numero):
        if numero % i == 0:
            num = num + i
    x = True
    if numero == 1:
        x = False
        
    for i in range(2, numero):
        if numero % i == 0:
            x = False
    return(num,x)
            
numero = 8
print(suma_divisores(numero))
           