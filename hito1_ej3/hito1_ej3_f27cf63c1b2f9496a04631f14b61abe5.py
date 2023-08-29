#Aprobación de créditos
ing = int(input("ingrese su ingreso: "))
ano = int(input("ingrese su año de nacimiento: "))
hij = int(input("ingrese numero de hijos: "))
per = int(input("ingrese años de pertenencia al banco: "))
e_c = str(input("ingrese su estado civil: "))
viv = str(input("ingrese si vive en campo o ciudad: "))
edad=2022-1970
if (per>10 and hij>1):
    print("APROBADO")
elif (e_c=="C") and (hij>3) and (45<=(edad)<=55):
    print("APROBADO")
elif (ing>2500000) and (e_c=="S") and (viv=="U"):
    print("APROBADO")
elif (ing>3500000) and (per>5):
    print("APROBADO")
elif (viv=="R") and (e_c=="C") and (hij<2):
    print("APROBADO")
else:
    print("RECHAZADO")
        