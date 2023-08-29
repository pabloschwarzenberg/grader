#Aprobación de créditos
income=int(input("Ingreso (en pesos): "))
birth=int(input("Año de nacimiento: "))
children=int(input("Numero de hijos: "))
years=int(input("Años de pertenencia al banco: "))
civil=input("Estado civil: ")
place=input("Campo o ciudad: ")
# Procesamiento de credito
if(years>10):
    if(children>=2):
        print("APROBADO")
if(civil=="C"):
    if(children>=3):
        if(45<(2017-birth)<55):
            print("APROBADO")
if(income>2500000):
    if(civil=="C"):
        if(place=="S"):
            print("APROBADO")
if(income>3500000):
    if(years>5):
            print("APROBADO")
if(place=="R"):
    if(civil=="C"):
        if(children<2):
            print("APROBADO")
else:
    print("RECHAZADO")
