#Factores Primos
n=int(input("ingrese numero a descomponer: "))
i=2
while i < (n+1):
	while (n % i) == 0:
		print(i)
		n=n/i
	i+=1