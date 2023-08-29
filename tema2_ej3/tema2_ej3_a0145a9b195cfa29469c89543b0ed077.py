# Numero perfecto
# Declaración de la función
def numero_perfecto(n):
    sd = 0
    for i in range(1,n):
        if (n%i==0):
            sd = sd + i
    if sd==n:
        return True
    else:
        return False
# Programa principal
print("Números Perfectos")
n= int(input("Indique un número natural: "))
if numero_perfecto(n):
    print("El número indicado SI es Perfecto")
else:
    print("El número indicado NO es Perfecto")