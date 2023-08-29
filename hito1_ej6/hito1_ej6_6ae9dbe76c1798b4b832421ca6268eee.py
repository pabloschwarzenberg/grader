#Ordenar tres numeros de manera ascendente
a = int(input("Escribe el primer numero:"))
b = int(input("Escribe el segundo numero:"))
c= int(input("Escribe el tercer numero:"))

x = min(a,b,c)
y= max (a,b,c)
z = (a+b+c)-x-y

print(str(x)+"," + str(z)+ ","+str(y))