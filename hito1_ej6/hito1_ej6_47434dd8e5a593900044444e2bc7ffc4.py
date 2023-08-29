#Ordenar tres números
x=int(input("Ingrese un número entero: "))
y=int(input("Ingrese otro: "))
z=int(input("Coloque un tercer entero: "))
if x<=y<=z:
      print(str(x)+" , "+str(y)+" , "+str(z))
if x<=z<=y:
      print(str(x)+" , "+str(z)+" , "+str(y))
if y<=x<=z:
      print(str(y)+" , "+str(x)+" , "+str(z))
if y<=z<=x:
      print(str(y)+" , "+str(z)+" , "+str(x))
if z<=x<=y:
      print(str(z)+" , "+str(x)+" , "+str(y))
if z<=y<=x:
      print(str(z)+" , "+str(y)+" , "+str(x))