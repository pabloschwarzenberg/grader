#Aprobación de créditos
def aprobacionCredito(ingreso,anoNacimiento,hijos,anosBanco,estadoCivil,localidad):
  anos= 2022-anoNacimiento
  if anosBanco>10 and hijos>=2:
    return True
  elif estadoCivil=="C" and hijos>3 and 45<=anos<=55:
    return True
  elif ingreso>2500000 and estadoCivil=="S" and localidad=="C":
    return True
  elif ingreso>3500000 and anosBanco>5:
    return True
  elif localidad=="R" and estadoCivil=="C" and hijos<2:
    return True
  return False
ingreso=int(input())
anoNacimiento=int(input())
hijos=int(input())
anosBanco=int(input())
estadoCivil=input()
localidad=input()
if aprobacionCredito(ingreso,anoNacimiento,hijos,anosBanco,estadoCivil,localidad):
  print("APROBADO")
else:
  print("RECHAZADO")
