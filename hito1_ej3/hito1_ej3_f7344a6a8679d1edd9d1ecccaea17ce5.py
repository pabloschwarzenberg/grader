#Aprobación de créditos
ingreso=int(input("Cantidad de ingresos en pesos chilenos: "))
ADN= int(input("Ingrese su año de nacimiento: "))
AACTUAL= 2021-ADN
NHijos= int(input("¿Cuántos hijos tiene?: "))
AConElBanco= str(input("¿Cuántos años ha sido cliente en nuestro banco?: "))
EstadoCivil= str(input("Indique su estado civil (S/C): "))
V=str(input("Indique si vive en un sector rural o sector urbano(R/U): "))
if NHijos>= 2 and AConElBanco >= 10:
  print("APROBADO")
elif EstadoCivil=="C" and NHijos>3 and AACTUAL<=55 and AACTUAL>=45:
  print("APROBADO")
elif ingreso>=2500000 and EstadoCivil== "S" and V=="U":
  print("APROBADO")
elif V=="R" and EstadoCivil=="C" and NHijos<2:
  print("APROBADO")
elif ingreso>3500000 and AConElBanco>5:
  print("APROBADO")
else:
  print("RECHAZADO")