#Sistema de Ecuaciones
a=int(input("Ingrese el primer valor: "))
b=int(input("Ingrese el segundo valor: "))
c=int(input("Ingrese el tercer valor: "))
d=int(input("Ingrese el cuarto valor: "))
e=int(input("Ingrese el quinto valor: "))
f=int(input("Ingrese el sexto valor: "))

primera_x_parte_real=(d*c)
primera_x_parte_incognita=(d*b)
segunda_x_parte_real=(a*f)
segunda_x_parte_incognita=(a*e)

#primera incognita YYYY
primera_parte_solucion_y= segunda_x_parte_incognita - primera_x_parte_incognita #PARTE INCOGNITA
segunda_parte_solucon_y= segunda_x_parte_real - primera_x_parte_real #PARTE REAL
y = segunda_parte_solucon_y / primera_parte_solucion_y

#segunda incognita XXXXX
x= (c - (b*y))/a

x2=str(x)
y2=str(y)

print("x="+x2)
print("y="+y2)