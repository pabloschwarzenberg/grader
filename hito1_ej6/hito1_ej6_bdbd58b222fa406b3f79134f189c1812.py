#Ordenar tres números
x =int(input("ingrse el primer numero entero:") )
y =int(input("ingrse el segundo numero entero:") )     
z =int(input("ingrse el tercer numero entero:"))

a = min(x , y , z)
b = max(x , y , z)
c = (x + y + z) - a - b


print (a,",",c, ",",b)
