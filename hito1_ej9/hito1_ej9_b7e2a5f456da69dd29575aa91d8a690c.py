#Escribe un programa que resuelva un sistema de dos ecuaciones con dos incognitas.
#Tu programa recibirá los seis números reales que representan el sistema
#y deberá imprimir la dos soluciones redondeadas a un decimal. Ejemplo: Para el sistema 2x+3y=6 y x+2y=5,
#tu programa debe imprimir: x=-3.0 ,y=4.0
#Ecuación_1
a = float(input('Ingrese primer número: '))
b = float(input('Ingrese segundo número: '))
c = float(input('Ingrese tercer número: '))

#Ecuación_2
d = float(input('Ingrese cuarto número: '))
e = float(input('Ingrese quinto número: '))
f = float(input('Ingrese sexto número: '))

determinante = a*e - b*d
if determinante != 0:
    x = (c*e-b*f)/determinante
    y = (a*f-c*d)/determinante

else:
    print('No tiene solución')
print('x=',(round(x,1)))
print('y=',(round(y,1)))
