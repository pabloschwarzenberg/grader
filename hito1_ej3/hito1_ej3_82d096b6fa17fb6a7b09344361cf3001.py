#Programa para decidir la aprobación de un crédito

print ("Para decidir si su crédito es aprobado o no, deberá responder una serie de preguntas")

ing = int (input("Ingresa cual el monto de tus ingresos mensuales: "))
year = int (input("Ingresa tu año de nacimiento: "))
sons = int (input("Ingresa el número de hijos que tienes (si no tienes ingresa 0): "))
perm = int (input("Ingresa hace cuandos años perteneces a nuestro banco: "))
ec = str (input("Ingresa tu estado civil ( ""S"" para soltero y ""C"" para casado): "))
luvi = str (input("Ingresa una U si vives en una zona urbana o ingresa una R si vives en una zona rural: "))

edad = 2021 - year



#ඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞ

if int(perm) > int(10) and int(sons) >= int(2):
    print ("CREDITO APROBADO")
elif int(sons) >= int(3) and str(ec) == "C" and int(edad) in range(45, 55):
    print ("CREDITO APROBADO")
elif int(ing) >= int(2500000) and  str(ec) == "S" and str(luvi) == "U":
    print ("CREDITO APROBADO")
elif int(ing) >= int(3500000) and int(perm) >= int(5):
    print ("CREDITO APROBADO")
elif str(luvi) == "R" and str(ec) == "C" and int(sons) <= int(2):
    print ("CREDITO APROBADO")
else:
    print ("CREDITO RECHAZADO")