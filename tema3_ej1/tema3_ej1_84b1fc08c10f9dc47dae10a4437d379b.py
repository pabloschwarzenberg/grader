# completa el código de la función
def suma_divisores(a):
    div = []
    if a != 1:
        for i in range(1, a):
            if a%i == 0:
                div.append(i)
    else:
        div.append(0)
    
    suma = sum(div)
    
    if suma == 1:
        primo = True
    else:
        primo = False
    
    return suma, primo