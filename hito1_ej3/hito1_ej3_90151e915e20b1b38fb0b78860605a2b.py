#Aprobación de créditos
ing = int(input("digite sus ingresos : "))
ano = int(input("ingrese su año de nacimiento : "))
nh = int(input("digite el numero de hijos que tenga : "))
adp = int(input("ingrese los años de pertenencia al banco :"))
ec = input("estado civil S) soltero, C) casado : ")
viv = input("indique si vive U) urbano , R) rural : ")
ano2 = 2020 - ano
if adp > 10 and nh >= 2:
    print("APROBADO")

if ec == "C" or "c" and ano2 <= 55 and ano2 >=45:
    print("APROBADO")
    
if ing >= 2500000 and ec == "S" or "s" and viv == "U" or "u":
    print("APROBADO")
    
if ing >= 3500000 and adp > 5:
    print("APROBADO")
    
if viv == "R" or "r" and ec == "C" or "c" and nh < 2:
    print("APROBADO") 