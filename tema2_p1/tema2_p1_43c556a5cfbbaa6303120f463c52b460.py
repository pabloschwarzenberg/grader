# por favor escribe aquí tu función

def es_primo(numero):
    n = int(numero)
    i = 2 
    while 1 < i < n:
        i = int(i)
        if n%i == 0:
            return("False")

        elif n%i != 0:
            return("True")

numero = input("Numero: ")
print(es_primo(numero))
           