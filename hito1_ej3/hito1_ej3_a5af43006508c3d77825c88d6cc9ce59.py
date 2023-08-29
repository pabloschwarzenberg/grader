#Aprobación de créditos
i = int(input("Ingreso: "))
an = int(input("Año de nacimiento: "))
nh = int(input("Número de hijos: "))
ab = int(input("Año de pertenencia al banco: "))
ec = input("Estado Civil: ")
an = input("Campo o Ciudad: ")
if ab>10 and nh>=2:
     print("APROBADO")
elif ec == "C" and nh>=3 and 1977>=an>=1966:
    print("APROBADO")
elif i>2500000 and ec == "S" and an == "U":
    print("APROBADO")
elif i>3500000 and ab>5:
    print("APROBADO")
elif an == "R" and ec == "C" and nh<2:
    print("APROBADO")
else:
    print("RECHAZADO")