numero=int(input("Escriba un número entero: "))
while numero<=1:
    numero=int(input("el numero no es mayor que 1. Inténtelo de nuevo: "))
copia=numero

print("factores primos: ")
i=2
while i<copia:
    while copia%i==0:
        copia=copia//i
        print(i)
    i+=1
print(copia)      