#Conversión de Decimal a Binario
numero = int(input(""))
s = []
sum = 0
n = numero
a = 0
while(n > 0) : 
	s.append(n%2)
	n = n//2
s2 = s[::-1]	
for i in s :
	sum = sum + i*(10**a)
	a = a + 1
print("resultado=",sum)