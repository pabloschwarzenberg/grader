#Aprobación de créditos
ing = int(input("Ingresos: "))
año_nac = int(input("Año de Nacimiento: "))
hijos = int(input("Numero de hijos: "))
año_banco = int(input("Año de pertenencia al banco: "))
est = str(input("Estado Civil: "))
vive = str(input("Campo o ciudad: "))

if año_banco > 10 and 2 <= hijos:
    print ("APROBADO")

elif est == "C" and hijos > 3 and 1965 < año_nac < 1975:
    print ("APROBADO")

elif ing > 2500000 and est == "S" and vive == "U":
    print ("APROBADO")

elif ing > 3500000 and año_banco > 5:
    print ("APROBADO")

elif vive == "R" and est == "C" and hijos < 2:
    print ("APROBADO")

else:
    print ("RECHAZADO")    