#Ordenar tres números
#Ordenar 3 numeros
uno=int(input("Ingrese un numero entero: "))
dos=int(input("Ingrese un numero entero: "))
tres=int(input("Ingrese un numero entero: "))
menor=0
intermedio=0
mayor=0
if(uno<=dos and uno<=tres):
    menor=uno
if(dos<=uno and dos<=tres):
    menor=dos
if(tres<=dos and tres<=uno):
    menor=tres
if(uno<=dos and uno>=tres) or (uno>=dos and uno<=tres):
    intermedio=uno
if(dos<=uno and dos>=tres) or (dos>=uno and dos<=tres):
    intermedio=dos
if(tres<=dos and tres>=uno) or (tres>=dos and tres<=uno):
    intermedio=tres
if(uno>=dos and uno>=tres):
    mayor=uno
if(dos>=uno and dos>=tres):
    mayor=dos
if(tres>=dos and tres>=uno):
    mayor=tres
print(menor,",",intermedio,",",mayor)      