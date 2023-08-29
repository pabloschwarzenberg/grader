#Descomponer un número
n = int(input("Ingresa un número de hasta 4 dígitos: "))
u = n // 1%10
d = n // 10%10
c = n // 100%10
m = n // 1000%10

print("{}M + ".format(m), end="")
print("{}C + ".format(c), end="")
print("{}D + ".format(d), end="")
print("{}U".format(u), end="")
