#Descomponer un número
print("SOLO PARA NÚMEROS dE 4 DIGITOS")

n = int(input("Ingrese un número: \n"))
u = n // 1 % 10
d = n // 10 % 10
c = n // 10**2 % 10
m = n // 10**3 % 10

print("{}M + {}C + {}D + {}U".format(m,c,d,u))

        