#Sistema de Ecuaciones
x1 = int(input("Ingrese un numero x"))
y1 = int(input("Ingrese un numero y"))
r1 = int(input("Ingrese un resultado para la primera ecuacion "))
x2 = int(input("Ingrese un numero x"))
y2 = int(input("Ingrese un numero x"))
r2 = int(input("Ingrese un resultado para la segunda ecuacion "))
inverso= -x1
mul_x2= inverso*x2
mul_y2= inverso*y2
mul_r2= inverso*r2
resultado1 = x1 + mul_x2
resultado2 = y1 + mul_y2
resultado3 = r1 + mul_r2
y = resultado3/resultado2
x = (r1 + (y1*y*-1))/x1
resultado_x = "x=" + str(x)
resultado_y = "y=" + str(y)
lista = []
lista.append(resultado_x)
lista.append(resultado_y)
print(lista)