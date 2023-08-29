#Descomponer un número
numero=int(input("Ingresa un numero de 4 digitos:"))
miles=numero//10**3
centenas=numero//10**2%10
decenas=numero%10**2//10
unidades=numero%10
print(str(miles)+"M"+"+"+str(centenas)+"C"+"+"+str(decenas)+"D"+"+"+str(unidades)+"U")