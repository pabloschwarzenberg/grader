#descomponer un numero
n = int(input("Ingrese un numero de 4 digitos: "))
m = n//1000
d = n//100
d = d%10
c = n//10
c = c%10
u = n%10

print("{}M + {}C + {}D + {}U".format(m,d,c,u))
