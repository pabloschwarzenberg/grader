#Descomponer un número
print ("Introduce el número: ")
numero = int(input ())

M = numero / 1000
tmp = numero % 1000

C = tmp / 100
tmp = tmp % 100

D = tmp / 10
U = tmp % 10
print ("%iM+" % M ,"%iC+" % C,"%iD+" % D ,"%iU" % U)

