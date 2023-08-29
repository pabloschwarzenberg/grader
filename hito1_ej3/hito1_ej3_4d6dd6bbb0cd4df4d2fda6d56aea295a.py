#Aprobación de créditos
ingreso=input("inserte ingreso monetario: ")
nacimiento=input("ingrese año de nacimiento: ")
edad=2018-int(nacimiento)
canthijos=input("ingrese numero de hijos: ")
añosbanco=input("ingrese años en el banco: ")
estcivil=str(input("ingrese estado civil (C-S): "))
residencia=str(input("ingrese residencia (U-R): "))

if int(añosbanco)>10 and int(canthijos)>=2:
    print("APROBADO")
elif str(estcivil)==str("C") and int(canthijos)>3 and int(edad)<55 and int(edad)>45:
    print("APROBADO")
elif int(ingreso)>2500000 and str(estcivil)==str("S") and str(residencia)==str("U"):
    print("APROBADO")
elif int(ingreso)>3500000 and int(añosbanco)>5:
    print("APROBADO")
elif str(residencia)==str("R") and str(estcivil)==str("C") and int(canthijos)<2:
    print("APROBADO")
else:
    print("RECHAZADO")      