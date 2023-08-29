# completa el código de la función
def suma_divisores(numero):
    lista= []

        
    for i in range(1, numero):
        if (numero % i == 0):
            lista.append(i)
    suma = sum(lista)
    if suma == 1:
        return (suma, True)
    else:
            
        return (suma, False)
        

           