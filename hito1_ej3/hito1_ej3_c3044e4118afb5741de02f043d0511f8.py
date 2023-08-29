#Aprobación de créditos
a = int(input("Ingrese su ingreso (en pesos) --> "))
b = int(input("Ingrese el año de nacimiento --> "))
c = int(input("Ingrese el numero de hijos/as --> "))
d = int(input("Ingrese años de pertenecia al banco --> "))
e = input("Ingrese su estado civil S=Soltero - C=Casado  --> ")
f = input("Ingrese si vive en el campo o ciudad U=urbano - R=rural --> ")

si = 0
año = 2021 - b
banco = 2021 - d

if d > 10 and c > 1:
    print("Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos.")
    si = 1
    
if e == "C" and c > 3 and (año > 44 and año < 56):
    print("Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.")
    si = 1
    
if a > 2500000 and e == "S" and f == "U":
    print("Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.")
    si = 1
    
if a > 3500000 and banco > 5:
    print("Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años")
    si = 1
    
if f == "R" and e == "C" and c < 2:
    print("Si el cliente vive en el campo, es casado y tiene menos de dos hijos.")
    si = 1

if si == 1:
    print("APROBADO")

else:
    print("RECHAZADO")
    

   