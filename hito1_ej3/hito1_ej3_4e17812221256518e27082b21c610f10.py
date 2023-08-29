#Aprobación de créditos
ingreso=eval(input("ingrese su ingreso")) 
agno_nacimiento=eval(input("ingrese su año de nacimiento"))
numero_hijos=eval(input("ingrese su numero de hijos"))
agnos_pertenencia_banco=eval(input("numero de años de pertenencia al banco"))
estado_civil=str(input("(S:soltero, C:casado)"))
vivienda=str(input("(U:urbano, R:rural)"))

edad=2020-agno_nacimiento

if(agnos_pertenencia_banco>=10 and numero_hijos>=2):
    print("APROBADO")
    
elif (estado_civil=="C") and (numero_hijos>=3) and (45<=edad<=55):
     print("APROBADO")

elif ingreso>=2500000 and estado_civil=="S" and vivienda=="U": 
     print("APROBADO")
     
elif ingreso>=3500000 and agnos_pertenencia_banco>=5:
     print("APROBADO")
     
elif vivienda=="R" and estado_civil=="C" and numero_hijos<=2:
     print("APROBADO")
     
else:
    print("RECHAZADO")

