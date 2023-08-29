numero1 = int(input("Ingrese numero 1:")) #x
numero2 = int(input("Ingrese  numero 2:")) #y
numero3 = int(input("Ingrese  numero 3:"))
numero4 = int(input("Ingrese  numero 4:")) #x
numero5 = int(input("Ingrese  numero 5:")) #y
numero6 = int(input("Ingrese  numero 6:"))

n1=numero1 
n2=numero2 
nn2=numero2 
n3=numero3
n4=numero4
n5=numero5
n6=numero6

numero1 = numero4*(-1)*numero1
numero2 = numero4*(-1)*numero2
numero3 = numero4*(-1)*numero3
numero4 = n1*numero4
numero5 = n1*numero5
numero6 = n1*numero6

sumaX = numero1 + numero4
sumay = numero2 + numero5
suma = numero3 + numero6

print("Suma de la x",sumaX)
print("Suma de la y",sumay)
print("Suma de la x",suma)

y = round(suma/sumay,1)



n1 = -n5*n1
n2 = -n5*n2
n3 = -n5*n3
n4 = nn2*n4
n5 = nn2*n5
n6 = nn2*n6

sumaX = n1 + n4
sumay = n2 + n5
suma = n3 + n6

x = round(suma/sumaX,1)
print("x=", x)
print("y=", y)