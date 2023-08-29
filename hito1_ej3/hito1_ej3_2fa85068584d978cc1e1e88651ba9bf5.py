#Aprobación de créditos
#Datos base

a = int(input("Indique sus ingresos en pesos: $"))
b = int(input("Ingrese su año de nacimiento: "))
edad = (int(2022)-b)
bb = print("Su edad es:  ",edad)
c = int(input("Ingrese cantidad de hijos: "))
d = int(input("Ingrese cantidad años de pertenencia en el banco: "))

#estado civil#
print("Ingrese su estado civi:")
print(" S = Soltero \n C = Casado")
e = str(input("Ingrese su respuesta (S o C):  "))
if e == str("S"):
    print("Estado civil: Soltero")
elif e == str("C"):
    print("Estado civil: Casado")

S = str("S")
C = str("C")

#Vivienda
print("Ingrese donde vive:")
print(" U = Urbano \n R = Rural")
f = str(input("Ingrese su respuesta (U o R):  "))
U = str("U")
R = str("R")

if f == str("U"):
    print("Vivienda: Urbana")
elif f == str("R"):
    print("Vivienda: Rural")

#Decisión de aprobación de crédito
if d > 10 and c >= 2:
    print("APROBADO")
# Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.
elif e == str(S) and c >= int(3) and (int(45)<=bb<=int(55)):
    print("APROBADO")
# Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
elif a > int(2500000) and e == str("S") and f == str("U"):
    print("APROBADO")
#Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
elif a > int(3500000) and d > int(5):
    print("APROBADO")
#Si el cliente vive en el campo, es casado y tiene menos de dos hijos.
elif f == str("R") and e ==str("C") and c < int(2):
    print("APROBADO")
else: 
    print ("RECHAZADO")
