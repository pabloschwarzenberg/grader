#Aprobación de créditos
ingreso= int(input("Su ingreso en pesos: "))
ano_naci= int(input("Año de nacimiento: "))
hi_jos= int(input("Ingrese el numero de hijos: "))
ano_pert= int(input("Ingrese los años de pertenecia al banco: "))
estado_civil= str(input("Ingrese su estado civil: ")) 
rural_urban= str(input("Ingrese si vive en zona Urbana o Rural: "))

if (10 < ano_pert)and (2 <= hi_jos):
    print("APROBADO")
elif(estado_civil == "C")and (3 < hi_jos) and (1965 < ano_naci < 1977):
    print("APROBADO")
elif(2500000 < ingreso)and (estado_civil == "S")and (rural_urban == "U"):
    print("APROBADO")  
elif (3500000 < ingreso) and (5 < ano_pert):
    print("APROBADO")
elif (rural_urban == "R") and (estado_civil == "C")and (hi_jos < 2):
    print("APROBADO")
else:
    print("RECHAZADO")     