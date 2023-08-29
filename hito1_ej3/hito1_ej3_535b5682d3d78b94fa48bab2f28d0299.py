#Ingreso (en pesos)
#Año de nacimiento
#Número de hijos
#Años de pertenencia al banco
#Estado civil ("S": soltero, "C", casado)
#Si vive en campo o cuidad ("U": urbano, "R": rural)
I=int(input("Ingrese su ganancia en pesos chilenos "))
AN=int(input("Ingrese su año de nacimiento "))
NH=int(input("Ingrese la cantidad de hijos tiene: "))
AP=int(input("Ingresar el tiempo de pertenencia al banco "))
EC=input("Ingrese S si esta soltero o C si esta casado ")
UR=input("Ingrese la letra U en la ciudad o R si vive en el campo ")
#Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos.
#Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.
#Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
#Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
#Si el cliente vive en el campo, es casado y tiene menos de dos hijos.
Edad=2022-AN
if(AP>10 and NH>2):
    print("APROBADO")
if(EC=="C" and NH>3 and Edad>45 and Edad<55):
    print("APROBADO")
if(I>2500000 and EC=="S" and UR=="U"):
    print("APROBADO")
if(I>3500000 and AP>5):
    print("APROBADO")
if(UR=="R" and EC=="C" and NH<2):
    print("APROBADO")
else:
    print("rechazado")
    