#Aprobación de créditos
i=int(input("Ingreso: "))
an=int(input("Año de nacimiento: "))
nh=int(input("Número de hijos: "))
ap=int(input("Años de pertenencia al banco: "))
e=input("Estado civil: ")
cc=input("Vive en el campo o ciudad: ")

if ap>10 and nh>=2:
    print("APROBADO")
elif e=="C" and (1962<an and an<1972):
    print("APROBADO")
elif i>2500000 and e=="S":
    if cc=="U":
        print("APROBADO")
    else:
        print("RECHAZADO")
elif i>3500000 and ap>5:
    print("APROBADO")
elif cc=="R" and e=="C":
    if nh<2:
        print("APROBADO")
    else:
        print("RECHAZADO")
else:
    print("RECHAZADO")
    
    