#Aprobación de créditos
ingreso = eval(input("Ingreso: "))
año = eval(input("Año nacimiento: "))
añoReal = 2020 - año
nHijos = eval(input("Numero de hijos: "))
pBanco = eval(input("Años de pertenencia banco: "))
eCivil = input("Estado Civil: ")
uoR = input("Campo o ciudad: ")

if pBanco > 10 and nHijos >= 2:
    aprobar = True
elif eCivil == "C" and nHijos > 3 and 45 < añoReal < 55:
    aprobar = True
elif ingreso > 2500000 and eCivil == "S" and uoR == "U":
    aprobar = True
elif ingreso > 3500000 and pBanco > 5:
    aprobar = True
elif uoR == "R" and eCivil == "C" and nHijos < 2:
    aprobar = True

if aprobar:
    print("APROBADO")
else:
    print("RECHAZADO")      