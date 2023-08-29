# completa el código de la función
def suma_divisores(Numero):
    Suma = 0
    Suma2 = 0
    Contador = 0
    for I in range(1,Numero + 1):
        if Numero % I == 0 and Contador < 2:
            Suma += I
            Contador = Contador + 1
    for I in range(1,Numero):
        if Numero % I == 0:
            Suma2 += I 
    if Suma == Numero + 1:
        return Suma2,True
    else:
        return Suma2,False

def Menu():
    if __name__ == "__main__":
        N = int(input("Ingrese el numero: "))
        X = suma_divisores(N)
        if X[1] == True:
            return(X)
        else:
            return(X)

print(Menu())