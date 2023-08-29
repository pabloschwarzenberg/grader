#Ordenar tres números
a= int(input("ingrese un numero:"))
b= int(input("ingrese un numero:"))
c= int(input("ingrese un numero:"))

x= min(a,b,c)
z= max(a,b,c)
y= (a+b+c) - x - z

print("De menor a mayor:",x,",",y,",",z)
      