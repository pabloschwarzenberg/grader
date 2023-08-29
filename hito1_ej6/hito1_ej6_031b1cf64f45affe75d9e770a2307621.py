#Ordenar tres números
x = int(input (" ingrese el primer numero : " ))
y = int(input (" ingrese el segundo numero : " ))
z = int(input (" ingrese el tercer numero : " ))
if (x>=y>=z):
    lista1=[z,y,x]
    print (lista1)
if(x>=z>=y):
    lista2=[y,z,x]
    print (lista2)
if(z>=x>=y):
    lista3=[z,x,y]
    print (lista3)
if(z>=y>=x):
    lista4=[x,y,z]
    print (lista4)
if(y>=z>=x):
    lista5=[x,z,y]
    print (lista5)
if(y>=x>=z):
    lista6=[z,x,y]
    print (lista6)

