#Aprobación de créditos
   ingreso=int(input("Ingrese su sueldo liquido:"))
nacimiento=int(input("ingrese su Año de Nacimiento:"))
hjos=int(input("Ingrese numero de Hijos:"))
permanencia=int(input("ingrese su permanencia en el Banco:"))
civil=input("Ingrese su estado civil,S:SOLTERO,C:CASADO:")
lugar=input("Lugar de Residencia,U:URBANO,R:RURAL:")
anos=nacimiento-2020
if permanencia > 10 and hijos >=2:
    print("APROBADO")
elif civil == 'C' or civil == 'c' and hijos > 3:
    print("APROBADO")
elif ingreso > 2500000 and civil == 's' or civil == 'S' and lugar == 'U' or lugar=='u':
     print("APROBADO")
elif ingreso >3500000 and permanencia > 5:
     print("APROBADO")
elif lugar == 'U' or lugar == 'u' and hijos < 2:
     print("CLIENTE APROBADO")
else:
    print("CLIENTE RECHAZADO")
        