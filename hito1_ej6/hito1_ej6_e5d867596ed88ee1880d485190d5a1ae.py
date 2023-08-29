#ENTRADA

x = int(input("escriba el primer numero:"))
y = int(input("escriba el segundo numero:"))
z = int(input("escriba el tercer numero:"))

#DESARROLLO

a = min (x,y,z)
c = max(x,y,z)

b = (x + y + z) -(a+c)

#SALIDA

print ("los numeros de menor a mayor son:",a,",",b,",",c,)
