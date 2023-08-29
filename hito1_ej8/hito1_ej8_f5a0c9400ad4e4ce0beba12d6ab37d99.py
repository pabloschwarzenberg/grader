#Descomponer un número
numero = int(input("ingrese numero de hasta 4 cifras:"))
mil = (numero//1000)
cent = (numero//100)%10
dec = (numero//10)%10
uni = (numero//1)%10
print("Numero descompuesto:", mil,"M+", cent,"C+", dec,"D+", uni,"U")