# por favor escribe aquí tu función
def es_primo(numero):
    flag = 1  # Por defecto es primo
    if numero > 2:
        for W in range(2, numero): #Revisa si el número es divisible desde el 2 en adelante
            if (numero % W == 0):
                flag = 0 #Si pasa por aquí NO es primo
                break
    else:
        if numero==2:
            flag = 1 # el número 2 es primo (verdadero)
        else:
            flag = 0 #Es falso cuando numero es <= que 1

 

    if flag == 0:
        return False
    else:
        return True
           