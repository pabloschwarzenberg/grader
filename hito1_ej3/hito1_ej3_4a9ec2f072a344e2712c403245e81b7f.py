ingreso = float(input("Ingrese su ingreso mensual: "))
annonac = int(input("Ingrese su año de nacimiento: "))
nhijos = int(input("Ingrese la cantidad de hijos: "))
annosasociados = int(input("Ingrese los años asociados al banco: "))
estado = 0
estado = input("Ingrese estado civil Soltero(S) O Casado(C): ")
while not ((estado=="S") or (estado=="C")):
    estado = input("ERROR, Ingrese estado civil Soltero(S) o Casado(C): ")

zona = 0
zona = input("Ingrese donde vive zona Rural(R) o Urbana(U) : ")
while not ((zona =="R") or (zona =="U")):
   zona = input("ERROR, Zona Rural(R) o Zona Urbana(U): ")
annos = 2020 - annonac   
if (annosasociados >10 and nhijos >= 2):
    print("APROBADO")
elif estado =="C" and nhijos >3 and annos >= 45 and annos <=55:
     print("APROBADO")
elif ingreso >2500000 and estado =="S" and zona =="U":
     print("APROBADO")
elif ingreso >3500000 and annosasociados > 5:
     print("APROBADO")
elif zona =="R" and estado =="C" and nhijos < 2:
     print("APROBADO")
else:
     print("RECHAZADO")