#Aprobación de crédito
ingresos = int(input("Ingrese cantidad en pesos: "))
añoNacimiento = int(input("Ingrese año de nacimiento: "))
numHijos = int(input("Ingrese numero de hijos: "))
añosBanco = int(input("Ingrese años en el banco: "))
estadoCivil = str(input("Ingrese estado civil: "))
residencia = str(input("Ingrese si vive en zona U o R: "))
edad = 2021 - añoNacimiento

if añosBanco >=10 and numHijos >= 2:
    print("APROBADO")
elif estadoCivil == "C" and numHijos >3 and 45 < edad < 55:
    print("APROBADO")
elif ingresos >2500000 and estadoCivil == "S" and residencia == "U" :
    print("APROBADO")
elif ingresos >3500000 and añosBanco >5:
    print("APROBADO")
elif residencia == "R" and estadoCivil == "C" and numHijos <2:
    print("APROBADO")
else:
    print("RECHAZ")
