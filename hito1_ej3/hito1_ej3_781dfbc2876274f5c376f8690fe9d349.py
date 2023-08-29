#Aprobación de créditos
money=int(input("Ingresos:"))
a_nac=int(input("Año de Nacimiento:"))
num_h=int(input("Numero de Hijos:"))
a_per=int(input("Años de Pertenencia al Banco:"))
e_civil=str(input("Estado Civil:"))
ur_rur=str(input("Vive en sector Urbano o Rural:"))

a = 2021 - a_nac

if (a_nac > 10 and num_h >= 2):
    print("APROBADO")

elif(str(e_civil) == "C") and (num_h > 3) and (45 <= a <= 55):
    print("APROBADO")

elif(money > 2500000) and (str(e_civil)== "S") and (str(ur_rur) == "U"):
    print("APROBADO")
    
elif(money > 3500000) and (a_per > 5):
    print("APROBADO")

elif(str(ur_rur) == "R") and (str(e_civil) == "C") and (num_h < 2):
    print("APROBADO")

else:
    print("RECHAZADO")