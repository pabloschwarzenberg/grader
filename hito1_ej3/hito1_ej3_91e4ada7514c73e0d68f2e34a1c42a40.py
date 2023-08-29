#Aprobación de créditos
ing=int(input("Señale sus ingresos: "))
ano=int(input("Señale su año de nacimiento: "))
hijos=int(input("Señale cuántos hijos tiene: "))
ant=int(input("Señale su antigüedad como cliente: "))
civil=input("Señale su estado civil: ")
vive=input("Señale si vive en campo o ciudad ("U": urbano, "R": rural): ")

if ant>10 and hijos>=2:
    print("APROBADO")
if civil=="C" and hijos>3 and 1968<=ano<=1978:
    print("APROBADO")
if ing>2500000 and civil=="S" and vive=="U":
    print("APROBADO")
if ing>3500000 and ant>5:
    print("APROBADO")
if vive=="R" and civil=="C" and hijos<2:
    print("APROBADO")
else:
    print("REPROBADO")