#Factores Primos
def es_primo(numero):
    divisor = 1
    cantidaddivisores = 0
    while divisor <= numero:
        if numero % divisor == 0:
            cantidaddivisores = cantidaddivisores + 1
            divisor = divisor + 1

        else:
            divisor = divisor + 1
    if numero==2:
        return True

    if cantidaddivisores == 2:
        return True
    else:
        return False

def descomponer(numero):
    divisorp=1
    final= numero
    while divisorp<final:
        if es_primo(divisorp):
            while numero%divisorp==0:
                print(divisorp)
                numero=numero//divisorp
            divisorp = divisorp + 1  
        else:
            divisorp=divisorp+1
    if numero == 2:
                print(2)



n=int(input("Dime un numerito: "))
descomponer(n)
