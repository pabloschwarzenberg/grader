#Descomponer un número
numero = int(input("ingrese un numero de hasta 4 digitos:"))
w = numero// 1000
x = numero// 100%10
y = numero// 10%10
z = numero// 1%10

strA= w
strB= x
strC= y
strD= z

print(strA, "M+" , strB, "C+" , strC, "D+" , strD, "U")