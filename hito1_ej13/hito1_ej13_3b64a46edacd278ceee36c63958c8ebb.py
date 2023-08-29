#Factores Primos
lista = []
mult = 1
i = 2
numero = int(input("Ingrese numero"))
memorynum = numero
def es_primo(numero):
	s1 = []
	for i in range(numero) :
		if(numero%(i+1) == 0) :
			s1.append(i+1)
			i = i + 1
	if(len(s1) == 2) : es = True
	else : es = False
	return(es)
while(mult != numero):
	if (es_primo(i)):
		if(memorynum%i == 0):
			lista.append(i)
			memorynum = memorynum//i
			mult = mult * i
		else:
			i +=1
	else:
		i +=1
for i in lista:
	print(i)