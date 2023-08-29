n = int(input("ingrese numero:"))
def es_primo(n):
    contador = 0
    resultado = True
    for i in range(1,n+1):
        if(n%i == 0):
            contador += 1
        if (contador > 2):
            resultado = False
            break
        return resultado
if(es_primo(n) == True):
    print("el numero es primo")
else:
    print("el numero no es primo")