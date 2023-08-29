x = int(input("ingrese primer numero: "))
y = int(input("ingrese segundo numero: "))
z = int(input("ingrese tercer numero: "))
if(x>y and y>z):
  print(x,",",y,",",z)
elif(y>=x and x>=z):
    print(z,",",x,",",y)
elif(z>=x and x>=y):
    print(y,",",x,",",z)
elif(z>=y and y>=x):
    print(x,",",y,",",z)
elif(x>=z and z>=y):
    print(y,",",z,",",x)
elif(y>=z and z>=x):
    print(x,",",z,",",y)