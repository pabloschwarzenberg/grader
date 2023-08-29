print("Ingrese las variables de la primera ecuación\n")
x1=eval(input("ingrese el valor de X \n"))
y1=eval(input("ingrese el valor de y \n"))
z1=eval(input("ingrese el valor de Z \n"))
#segunda ecuación
print("Ingrese las variables de la segunda ecuación\n")
x2=eval(input("ingrese el valor de X \n"))
y2=eval(input("ingrese el valor de y \n"))
z2=eval(input("ingrese el valor de Z \n"))
#método de sutitución para 2x+3y=6 y x+2y=5
X=(z1-(3*y1)/2)
#sustituyendo Ecuación 2x+3y=6 y x+2y=5
X=round(z1-(y1*3),1)
Y=round(((z1-(X*2))/3),1)
print ("x=", X)
print ("y=",Y)