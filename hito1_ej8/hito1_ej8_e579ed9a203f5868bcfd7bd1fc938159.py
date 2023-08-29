#Descomponer un número
numero= int(input("Introduce el número: "))

M = numero / 1000
n = numero % 1000

C = n / 100
n  = n % 100

D = n / 10
U = n % 10

print("%iM" % M, "+", "%iC" % C,"+", "%iD" % D, "+", "%iU" % U)