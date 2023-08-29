#Aprobación de créditos
print("Test de credito")
sueldo = int(input("Ingrese su sueldo: "))
ano = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Ingrese la cantidad de hijos que tiene (Si no tiene, digite 0): "))
anosbanco = int(input("Ingrese la cantidad de años que lleva siendo cliente de nuestro banco: "))
estcivil = str(input("Indiquenos su estado civil (S:soltero, C:casado): "))
if estcivil=="S":
    estcivil="soltero"
if estcivil=="C":
    estcivil="casado"
locacion = str(input("¿Usted vive en zona urbana o rural? (U:urbana, R:rural): "))
anos = 2020-ano
#Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos.
if (anosbanco>10 and hijos>=2):
    print("APROBADO")
#Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.
if (estcivil=="casado" and hijos>3 and anos>=45 and anos<=55):
    print("APROBADO")
#Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
if (sueldo>2500000 and estcivil=="soltero" and locacion=="U"):
    print("APROBADO")
#Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
if (sueldo>3500000 and anosbanco>5):
    print("APROBADO")
#Si el cliente vive en el campo, es casado y tiene menos de dos hijos.
if(locacion=="R" and estcivil=="casado" and hijos<2):
    print("APROBADO")
else:
    print("RECHAZADO")
    print("APROBADO")
#Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.
if (estcivil=="casado" and hijos>3 and anos>=45 and anos<=55):
    print("APROBADO")
#Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
if (sueldo>2500000 and estcivil=="soltero" and locacion=="u"):
    print("APROBADO")
#Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
if (sueldo>3500000 and anosbanco>5):
    print("APROBADO")
#Si el cliente vive en el campo, es casado y tiene menos de dos hijos.
if(locacion=="r" and estcivil=="casado" and hijos<2):
    print("APROBADO")
else:
    print("RECHAZADO")      