#Aprobación de créditos
#variables
ingresos=int(input("Declare sus ingresos: $"))
nacimiento=int(input("Indique su año de nacimiento: "))
hijos=int(input("Indique numero de hijos: "))
apbanco=int(input("Indique sus años de pertenencia al banco: "))
estadocivil=str(input("Indique su estado civil, Soltero (s) o Casado (c): "))
zonaresidencia=str(input("Indique zona donde reside, Urbana (u) o Rural (r): "))
edad=2022-nacimiento
#resolucion
if apbanco>10 and hijos>=2 or estadocivil=="c" and hijos>3 and edad>=45 and edad<=55 or ingresos>2500000 and estadocivil=="s" and zonaresidencia=="u" or ingresos>350000 and apbanco>=5 or zonaresidencia=="r" and estadocivil=="c" and hijos<2:
  print("APROBADO")
else: print("RECHAZADO")