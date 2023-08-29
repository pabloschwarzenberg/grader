#Numeros perfectos
def numero_perfecto(Numero):
    Suma = 0
    for I in range(1,Numero):
        if Numero % I == 0:
            Suma += I
    if Numero == Suma:
        return 1
    else:
        return 0

def Menu():
    if __name__ == "__main__":
        N = int(input("Ingrese el numero: "))
        if numero_perfecto(N) == 1:
            return("Es un numero perfecto")
        else:
            return("No es un numero perfecto")

print(Menu())