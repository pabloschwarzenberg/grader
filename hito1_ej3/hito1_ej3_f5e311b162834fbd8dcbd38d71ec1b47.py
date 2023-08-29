#Aprobación de créditos
ingresoenpesos = int(input("ingreso en pesos"))
añodenacimiento = int(input("ingrse el año de nacimiento"))
numerosdehijos = int(input("ingrese el numeros de hijos"))
añosdepertenenciaenelbanco = int(input("años de pertenencia en el banco:"))
estadocivil = input("S:soltero,C:casado")
siviveencamponoenunaciudad = input("U:urbano,R:rural")
añosdeedad = 2022-añodenacimiento
if (10<añosdepertenenciaenelbanco and 2<=numerosdehijos):
    print(f"APROBADO")
elif (estadocivil == "C" and numerosdehijos>3 and 55>añosdeedad>45):
    print(f"APROBADO")
elif (ingresoenpesos>3500000 and añosdepertenenciaenelbanco>5):
    print(f"APROBADO")
else:
    print("RECHAZADO")
      