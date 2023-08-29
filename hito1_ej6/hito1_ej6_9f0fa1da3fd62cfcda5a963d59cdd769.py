#Ordenar tres números
x=int(input("ingrese un número entero:  "))
y=int(input("ingrese un número entero:  "))
z=int(input("ingrese un número entero:  "))
a= min(x,y,z)
c= max(x,y,z)
b= (x+y+z)-a-c
print(str(a)+ ","+str(b)+","+str(c))