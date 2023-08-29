# completa el código de la función
def suma_divisores(a):
    a = int(a)
    d = []
    suma = 0
    for i in range(1, a):
        if a%i == 0:
            d.append(i)
     
        elif a%i != 0:
            pass
    
    for i in d:
        suma = suma + i

    if suma == 1:
        print("primo")
        primo = True
    

    else:
        print("no es primo")
        primo = False

    return (suma, primo)
