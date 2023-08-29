#aprobacion de creditos
print("Ingrese sus datos para que su postulacion a un credito de consumo sea evaluada.\n-----------------------------------------------------------------")
Ingresos=int(input("Ingrese su sueldo en pesos: "))
Nacimiento=int(input("Ingrese su fecha de nacimiento: "))
Hijos=int(input("Ingrese cuantos hijos tiene: "))
AñosB=int(input("Ingrese cuantos años lleva con nosotros: "))
EC=input("Ingrese su estado civil (S para soltero. C para casado): ")
Re=input("Vive en zona rural o urbana (R para rural y U para urbana): ")
print("-----------------------------------------------------------------")
Edad=2022-Nacimiento
if AñosB>10 and Hijos>=2:
  print("APROBADO")
elif EC=="C" and Hijos>3 and Edad>45 and Edad<55:
  print("APROBADO")
elif Ingresos>2500000 and EC=="S" and Re=="U":
  print("APROBADO")
elif Ingresos>3500000 and AñosB>5:
  print("APROBADO")
elif Re=="R" and EC=="C" and Hijos<2:
  print("APROBADO")
else:
  print("RECHAZADO")