#Descompone un numero

numero = int(input("ingresa el numero de 4 digitos:"))

m = numero / 1000
tmp = numero % 1000

c = tmp / 100
tmp = tmp % 100

d = tmp / 10
u = tmp % 10

print ("Unidades de mil: %i" % m)
print ("Centenas: %i" % c)
print ("Decenas: %i" % d)
print ("Unidades: %i" % u)
print("%iM"%m,end="")
print("+%iC"%c,end="")
print("+%iD"%d,end="")
print("+%iU"%u)

