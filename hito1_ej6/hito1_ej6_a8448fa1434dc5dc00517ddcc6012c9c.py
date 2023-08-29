#Ordenar tres números
x=eval(input("ingresar numero 1",))
y=eval(input("ingresar numero 2",))
z=eval(input("ingresar numero 3",))
if(x>=y>=z):
  print("{},{},{}".format(z , y , x))
if(x>=z>=y):
  print("{},{},{}".format(y , z , x))
if(y>=x>=z):
  print("{},{},{}".format(z , x , y))
if(y>=z>=x):
  print("{},{},{}".format(x , z , y))
if(z>=x>=y):
  print("{},{},{}".format(y , x , z))
if(z>=y>=x):
  print("{},{},{}".format(y , x , z))



     