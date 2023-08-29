ingreso= int(input ("Cual es su salario al mes?: "))
year= int(input ("En que año naciste?: "))
hijos= int(input ("Cuantos hijos tiene?: "))
estadia= int (input ("Cuantos años lleva en nuestro banco?: "))
soC= (input ("Usted esta soltero(S) o casado (S): ")).upper()
uryRu= (input ("Usted vive en zona rural o urbana?")).upper()
if estadia > 10 and hijos >= 2:
    print("APROBADO")
elif soC == "C"  and hijos >= 3 and year >= 45 and year <= 55:
    print ("APROBADO")
elif ingreso > 2500000 and soC == "S" and uryRu == "U": 
     print ("APROBADO")
elif ingreso >= 3500000 and estadia > 5:
    print ("APROBADO")
elif uryRu == "R" and soC == "C" and hijos < 2: 
    print ("APROBADO")
else:
    print ("RECHAZADO") 