#Descomponer un número
numero=0
	
numero = int(input("Escribe un numero\n"))
   
millares = numero//10**3
c = numero//10**2
centenas = c%10**1
d = numero//10**1
decenas = d%10**1
unidades = numero%10**1

print(str(millares)+"M + " +str(centenas)+"C + " +str(decenas)+"D + " +str(unidades)+"U")

