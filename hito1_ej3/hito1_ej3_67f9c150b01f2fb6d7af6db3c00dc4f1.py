#Aprobación de créditos
Ingresos = int(input("Inserte sus ingresos"))
Nacimiento = int(input("Ingrese su año de nacimiento"))
Nhijos = int(input("Ingrese cantidad de hijos"))
AñosBanco = int(input("Ingrese años de pertenencia al banco"))
EstadoCivil = input("Ingrese su estado civil, S (soltero) o C (casado)")
Residencia = input("Ingrese si vive en campo o ciudad, U (urbano) o R (rural)") 
if AñosBanco>=10 and Nhijos>=2:
  Credito = print("APROBADO")
elif Nhijos>=3 and (1968<=Nacimiento<=1978):
  Credito = print("APROBADO") 
elif (Ingresos>=2500000 and EstadoCivil=="S") and Residencia==U:
  Credito = print("APROBADO")
elif Ingresos>=3500000 and AñosBanco>=5:
  Credito = print("APROBADO")
elif (Residencia=="R" and EstadoCivil=="C") and Nhijos<=2:
  Credito = print("APROBADO")
else: 
  Credito = print("RECHAZADO") 

print(Credito)       