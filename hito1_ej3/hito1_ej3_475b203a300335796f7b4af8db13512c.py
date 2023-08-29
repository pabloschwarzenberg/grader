print("por favor, ingrese los siguientes valores: ")
IN=int(input("Ingreso (en pesos): "))
AN=int(input("Año de nacimiento: "))
NH=int(input("Numero de hijos: "))
PB=int(input("Años pertenecientes al banco: "))
EC=input("estado civil: ")
if EC== "S" or EC== "C":
    print("dato valido")
elif EC!= "S" or EC!="C":
    print("dato invalido")
UR=input("vive en campo o ciudad: ") 
if UR== "R" or UR=="U":
   print("dato valido")
elif UR!= "R" or UR!="U":
    print("dato invalido")
if PB>10 and NH>=2:
    print("APROBADO")
elif EC=="C" and NH>3 and 2022-AN>=45 or 2022-AN<=55:
    print("APROBADO")
elif IN>2500000 and EC=="S" and UR=="U":
    print("APROBADO")
elif IN>3500000 and PB>5:
    print("APROBADO")
elif UR=="R" and EC=="C" and NH<2:
    print("APROBADO")
else:
    print("RECHAZADO")
      