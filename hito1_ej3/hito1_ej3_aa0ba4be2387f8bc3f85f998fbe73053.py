#Aprobación de créditos
print("Hola ingrese los datos del postulante porfavor")
ing = int(input("Ingreso: "))
year = int(input("Año de nacimiento: "))
hij = int(input("Número de hijos: "))
banye = int(input("Años de pertenencia al banco: "))
est = str(input("Estado civil: (S para soltero, C para casado)  "))
vive = str(input("sector donde habita: (U para urbano, R para rural)  "))

edad = 2022 - year
if(banye>10 and hij>=2):
    print("APROBADO")
elif(est=='C' and hij>3 and edad>45 and edad<55):
    print("APROBADO")
elif(ing>2500000 and est=='S' and vive=='U'):
    print("APROBADO")
elif(ing>3500000 and banye>5):
    print("APROBADO")
elif(vive=='R' and est=='C' and hij<2):
    print("APROBADO")
else:
    print("El postulante ha sido rechazado para el credito")
print("\n")