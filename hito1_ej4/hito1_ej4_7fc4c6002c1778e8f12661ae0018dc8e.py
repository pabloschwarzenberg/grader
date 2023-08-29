decimal = int(input("Ingrese el numero decimal que desea convertir en codigo binario: "))
binario = 0
n = 0
while decimal>0:
    digito = decimal%2
    decimal= int(decimal//2)
    binario = binario+digito*(10**n)
    n += 1
print("resultado=",binario)
