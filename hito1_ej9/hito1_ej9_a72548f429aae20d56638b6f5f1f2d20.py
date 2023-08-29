#Sistema de Ecuaciones
def ecuacion(x1,y1,z1,x2,y2,z2):
    y = ((z2*x1)-z1)/(-y1+(y2*x1))
    x = (z1-(y1*y))/x1
    return[x,y]

num = []
x = 0
while x < 6:
    numero = int(input("Ingrese número"))
    num.append(numero)
    x += 1

e = ecuacion(num[0], num[1], num[2], num[3], num[4],num[5])
print("x =", round(e[0], 1)), "\n", "y =", (round(e[1], 1))