#Aprobación de créditos
print("Bienvenido al sistema automatizado de créditos de consumo del banco de pelotillehue")

Ingreso=int(input("Indique su ingreso en pesos chilenos: "))
Nacimiento=int(input("Indique su año de nacimiento: "))
Hijos=int(input("Indique cuantos hijos tiene: "))
Pertenencia=int(input("Indique cuantos años de pertenencia lleva en el banco: "))
Civil=str(input("Indique su estado civil actual, en el caso de ser soltero ingrese S, en caso de estar casado ingrese C: "))
Vive=str(input("Indique si vive en el campo o la ciudad, en el caso de vivir en la ciudad ingresar U, en caso de vivir en un sector rural ingresar R: "))

if 10 < Pertenencia and 2 <= Hijos:
  print("APROBADO")

if Civil == "C" and 3 < Hijos and 45 < 2016-Nacimiento < 55:
    print("APROBADO")

if 2500000 < Ingreso and Civil == "S" and Vive == "U":
    print("APROBADO")

if 3500000 < Ingreso and 5 < Pertenencia:
    print("APROBADO")

if Vive == "R" and Civil == "C" and Hijos < 2:
    print("APROBADO")

else:
    print("REPROBADO")