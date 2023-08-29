#Aprobación de créditos
ingresos= int(input("sus ingreso en pesos: "))
edad= int(input("año en que nacio: "))
numero_hijos= int(input("número de hijos: "))
permanece_banco= int(input("años que pertenece al banco: "))
estado_civil = input("estado civil: ") .capitalize()
donde_vive= input("usted vive en campo o ciudad:").capitalize()
edad=2022 - int(edad)

if permanece_banco >= 10  and numero_hijos >= 2:
    print("APROBADO")
elif estado_civil== "C" and numero_hijos >3 and int(edad >=45) and str(edad <= 55):
    print("APROBADO")
elif ingresos >25000000 and estado_civil == "S" and donde_vive == "U": 
    print("APROBADO")
elif ingresos >35000000 and permanece_banco >5:
    print("APROBADO")
elif donde_vive == "R" and estado_civil == "C" and numero_hijos <2:
    print("APROBADO")
else:
    print("RECHAZADO")