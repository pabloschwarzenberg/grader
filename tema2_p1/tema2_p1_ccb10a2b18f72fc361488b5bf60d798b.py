import math
def es_primo(numero) :
    if (numero<=1):
        return False
    for i in range(2, math.ceil(math.sqrt(numero))+1):
        if(numero%i==0 and i!=numero):
            return False
        return True
while True:
    try:
        numero = int(input("inserta un numero: "))
        if numero ==0:
            break
        if es_primo(numero):
            print ("nEl numero es %s es primo" %  numero)
            break
        else:
            print("nEl numero %s No es primo" % numero)
            break
    except:
        print ("nEl numero tiene que ser entero")
        break