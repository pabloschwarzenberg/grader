x=int(input("Ingresa tu primer número: "))
y=int(input("Ingresa tu segundo número: "))
z=int(input("Ingresa tu tercer número: "))
if x>=y>=z:
    print(z,y,x)
elif x>=z>=y:
    print(y,z,x)
elif z>=x>=y:
    print(y,x,z)
elif z>=y>=x:
    print(x,y,z)
elif y>=z>=x:
    print(x,z,y)
elif y>=x>=z:
    print(z,x,y)


  

    