#Ordenar tres númmeros 
print("ingrese 3 valores")
a= int(input("ingrese el valor 1:"))
b= int(input("ingrese el valor 2:"))
c= int(input("ingrese el valor 3:"))

x = min(a, b, c)
z = max(a, b, c) 
y= (a+b+c)-(x+z)

print("los numeros ordenados de menor a mayor son:", x ,",",y,",",z)