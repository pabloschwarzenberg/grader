#Descomponer un número 
numero = int(input("ingrese un numero entre 1000 y 9999 : "))
x = numero // 1000
y = numero // 100%10
z = numero // 10%10
n = numero // 1%10
strA = x
strB = y
strC = z
strD = n

print(strA,"M+", strB,"C+", strC,"D+", strD,"U")
      