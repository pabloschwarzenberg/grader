#Sistema de Ecuaciones
num1 = float(input("ingrese los numeros 1:")) #x
num2 = float(input("ingrese los numeros 2:")) #y
num3 = float(input("ingrese los numeros 3:"))
num4 = float(input("ingrese los numeros 4:")) #x
num5 = float(input("ingrese los numeros 5:")) #y
num6 = float(input("ingrese los numeros 6:"))

n1=num1 
n2=num2 
nn2=num2 
n3=num3
n4=num4
n5=num5
n6=num6

#CALCULAR Y
num1 = num4*(-1)*num1
num2 = num4*(-1)*num2
num3 = num4*(-1)*num3
num4 = n1*num4
num5 = n1*num5
num6 = n1*num6

sumaX = num1 + num4
sumay = num2 + num5
sumaS = num3 + num6

print("Suma de la x",sumaX)
print("Suma de la y",sumay)
print("Suma de la x",sumaS)
#DEterminar la y    
y = round(sumaS/sumay,1)


#CALCULAR x
n1 = -n5*n1
n2 = -n5*n2
n3 = -n5*n3

n4 = nn2*n4
n5 = nn2*n5
n6 = nn2*n6

sumaX = n1 + n4
sumay = n2 + n5
sumaS = n3 + n6

#DEterminar la y    
x = round(sumaS/sumaX,1)

print("x=", x)
print("y=", y)