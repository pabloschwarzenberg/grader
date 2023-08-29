#Conversión de Decimal a Binario
n = int(input("Ingrese un numero hasta 2 digitos:"))
x = int(n)//2
x1 = x  //2
x2 = x1 //2
x3 = x2 //2
x4 = x3 //2

a = x4 % 2 
b = x3 % 2
c = x2 % 2
d = x1 % 2
e = x % 2
f = n % 2

print("resultado=",a,b,c,d,e,f)
