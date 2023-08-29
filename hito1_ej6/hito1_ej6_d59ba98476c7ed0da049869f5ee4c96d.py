#Ordenar tres números
x=int(input("Ingresa un número "))
y=int(input("Ingresa otro número "))
z=int(input("Ingresa un último número "))
if((x<=y) and (x<=z)):
    menor=x;
    if(y<=z):
      medio=y;
      mayor=z;
    else:
      medio=z;
      mayor=y;
elif((y<=x) and (y<z)):
    menor=y;
    if(x<=z):
      medio=x;
      mayor=z;
    else:
      medio=z;
      mayor=x;
else:
    menor=z;
    if(x<=y):
      medio=x;
      mayor=y;
    else:
      medio=y;
      mayor=x;
print(menor,",",medio,",",mayor)