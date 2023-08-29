ingreso=int(input("Ingreso en pesos: "))
año=int(input("Ingrese su año de nacimiento: "))
hijos=int(input("Ingrese su numero de hijos: "))
añosbanco=int(input("Ingrese su año de pertenencia en el banco: "))
estadocivil=input("Ingrese su estado civil (S/C): ")
lugar=input("Vive en Campo o Ciudad (U/R): ")
if(añosbanco>=10 and hijos>=2):
    print("APROBADO")
elif(estadocivil=="C" and hijos>=3 and 45<2020-año<55):
    print("APROBADO")
elif(ingreso>=2500000 and estadocivil=="S" and lugar=="U"):
    print("APROBADO")
elif(ingreso>=350000 and añosbanco>=5):
    print("APROBADO")
elif(lugar=="R" and estadocivil=="C" and hijos>=2):
    print("APROBADO")
else: (print("RECHAZADO"))


