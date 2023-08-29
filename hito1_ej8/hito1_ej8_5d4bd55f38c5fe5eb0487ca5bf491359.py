#Descomponer un número
numero=int(input('ingrese un numero: '))

M = numero//1000
numero = numero-M*1000
C = numero//100
numero =numero-C*100
D = numero//10
U = numero-D*10

a = str(M)+'M + '
b = str(C)+'C + '
c = str(D)+'D + '
d = str(U)+'U'
if M == 0:
	a = ''


final = a+b+c+d
print(final)
     