a = int(input("Escriba el primer numero : "))
b = int(input("Escriba el segundo numero : "))
c = int(input("Escriba el tercer numero : "))

d = min(a, b, c)
f = max (a, b, c)
e = (a + b + c) - d - f 

print("Los numeros en orden son: {}, {}, {} ".format(d, e, f))