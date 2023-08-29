#Conversión de Decimal a Binario

num=int(input("Ingrese un numero: "))
resto= 0
binario=""
while num >= 2:
	resto = num % 2
	num =  int(num / 2)
	binario = binario + str(resto)

aux = ""
largo = len(binario)
cont=0
aux=str(num)

while cont < largo:
	aux = aux + binario[largo - (cont + 1)]
	cont = cont + 1 

print("Resultado=",aux)