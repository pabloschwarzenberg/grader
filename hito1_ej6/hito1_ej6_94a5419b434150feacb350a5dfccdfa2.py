#Ordenar tres números
A = eval(input("ingrese un número: "))
B = eval(input("ingrese un número: "))
C = eval(input("ingrese un número: "))
#Orden
Ma = max(A,B,C)
print("el número mayor es: ", Ma)
Me = min(A,B,C)
print("el número menor es: ", Me)

D = (A + B + C) - Ma - Me
print("De menor a mayor el órden es ", Me," , " , D , " , ", Ma)