# por favor escribe aquí tu función
import math
def es_primo(numero):
    """
    Funcion que determina si un numero es primo
    Tiene que recibir el numero entero
    """
    # Para que un numero sea primo, unicamente tiene que dividirse dos veces:
    #   1 - divisible entre 1
    #   2 - divisible entre el mismo
    # En este bucle, empezamos por el dos hasta un numero anterior a el, por lo
    # que si en el bucle, alguna vez se divide el numero, quiere decir que no es
    # primo
    if (numero<=1):
        return False
 
    for i in range(2, math.ceil(math.sqrt(numero))+1):
        if(numero%i==0 and i!=numero):
            return False
    return True
True:
    try:
        numero = int(input("inserta un numero  "))
        if es_primo(numero):
            print ("El numero %s es primo" % numero)
        else:
            print ("El numero %s NO es primo" % numero)
    except:
        print ("El numero tiene que ser entero")