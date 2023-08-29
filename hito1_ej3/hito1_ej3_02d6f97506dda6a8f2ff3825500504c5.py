#Aprobación de créditos
ingreso= eval(input("Cuál es el ingreso de cliente en pesos: "))
ano_nacimiento= eval(input("Ingrese año de nacimiento:  "))
hijos= int(input("Ingrese cantida de hijos: "))
anos_banco= eval(input("Ingrese años de pertenencia al banco: "))
estado_civil= input("Estado civi: S: soltero C: Casado ")
donde_vive= input("Indique zona donde vive:  U: urbano R: rural ")

if anos_banco >10 and hijos >=2:
    print ("APROBADO")
elif (estado_civil == "C") and (hijos > 3) and (ano_nacimiento >= 45 and ano_nacimiento <=55):
    print ("APROBADO")
elif (ingreso > 2500000) and (estado_civil == "S") and (donde_vive == "U"):
    print ("APROBADO")
elif (ingreso > 3500000) and (anos_banco > 5):
    print ("APROBADO")
elif (donde_vive == "R") and (estado_civil == "C") and ( hijos < 2) :
    print ("APROBADO")
else:
    print ("RECHAZADO")