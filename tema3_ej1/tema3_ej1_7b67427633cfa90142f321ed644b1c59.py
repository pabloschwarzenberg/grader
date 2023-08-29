# completa el código de la función
def suma_divisores(a):
    divisores = []
    for i in range(1,a):
        if a% i == 0:
            divisores.append(i)
    return sum(divisores)

def es_primo(a):
    contador = 0
    for i in range(1, a):
        if a % i == 0:
            contador+= 1
    if contador == 2:
        return True
    else:
        return False
total = suma_divisores(1),es_primo(1)
total2 = suma_divisores(8),es_primo(8)
total3= suma_divisores(13),es_primo(13)
print(total)
print(total2)
print(total3)







        
           