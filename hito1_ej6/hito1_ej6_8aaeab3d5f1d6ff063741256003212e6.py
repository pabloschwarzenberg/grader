#Ordenar tres número
a= int(input("ingrese un numero:"))
b= int(input("ingrese su segundo numero:"))
c= int(input("ingrese su tercer numero:"))
MI= min (a,b,c)
MA= max (a,b,c)
d= (a + b + c) - MI - MA
print("el orden de menor a mayor es:", MI,",", d,",", MA)