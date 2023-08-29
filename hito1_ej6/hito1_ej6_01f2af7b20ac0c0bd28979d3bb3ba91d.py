n = eval(input("ingrese un numero natural"))
a = eval(input("ingrese un numero natural"))
s = eval(input("ingrese un numero natural"))

q =min (n,a,s)
c =max (n,a,s)
b= (n + a + s) - q - c 

print(sorted([q, c, b]))