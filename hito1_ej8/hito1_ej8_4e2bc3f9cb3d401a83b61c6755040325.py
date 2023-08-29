#Descomponer un número
num = int(input("ingrese un numero entre 1000 y 9999 : "))
x = num // 1000
y = num // 100%10
z = num // 10%10
n = num // 1%10
strA = x
strB = y
strC = z
strD = n

print(strA,"M + ", strB,"C + ", strC,"D + ", strD,"U")      