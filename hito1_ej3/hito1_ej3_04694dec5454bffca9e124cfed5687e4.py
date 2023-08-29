#Aprobación de créditos
ingreso = int(input("sus ingresos: "))
nacimiento = int(input("año de nacimiento: "))
hijos = int(input("numero de hijos: "))
anosenelbanco= int(input("cuantos años lleva afiliado al banco: "))
estadocivil = input("estado civil S:soltero C:casado: ")
zona= input("zona donde vive U:urbana  R:rural: ")
edad = 2022 - nacimiento

if(anosenelbanco > 10 and hijos >= 2):
    print("FELICIDADES CREDITO APROBADO")
elif(estadocivil=="c" and hijos > 3 and edad > 45 and edad < 55):
    print("FELICIDADES CREDITO APROBADO")
elif(ingreso>2500000 and estadocivil == "s" or estadocivil == "S" and zona == "U" or zona == "u" ):
    print("FELICIDADES CREDITO APROBADO")
elif(ingreso>3500000 and anosenelbanco > 5):
    print("FELICIDADES CREDITO APROBADO")
elif(estadocivil == "C" and hijos < 2 and zona== "R" or zona== "r"):
    print("FELICIDADES CREDITO APROBADO")
else:
    print("SU CREDITO A SIDO RECHAZADO:C")