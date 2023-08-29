#Aprobación de créditos
Ingreso=float(input("Ingresos mensuales: "))
ANacimiento=int(input("Año de nacimiento: "))
NumeroHijos=int(input("Numero de hijos: "))
APertenecienteBanco=int(input("Años de antiguedad en el banco: "))
EstadoCivil=input("Estado civil;C-'casado', S-'soltero'")
Ubicacion=input("ubicacion: U-'urbano, R,'rural")
Años=-2022
EstadoCivil=EstadoCivil.upper()
Ubicacion=Ubicacion.upper()
#desarrollo del credito
if APertenecienteBanco>10 and NumeroHijos>=2:
  print("APROBADO")
elif EstadoCivil.upper()=="C" and NumeroHijos>3 and años>=45 and años<=55:
  print("APROBADO")
elif Ingreso>2500000 and EstadoCivil.upper()=="S" and Ubicacion.upper()=="U":
  print("APROBADO")
elif APertenecienteBanco>5 and Ingreso>3500000:
  print("APROBADO")
elif Ubicacion.upper()=="R" and EstadoCivil.upper()=="C" and NumeroHijos<2:
  print("APROBADO")