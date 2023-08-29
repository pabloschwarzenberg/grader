#Aprobación de créditos
ingreso=int(input("su ingreso: "))
an=int(input("año de nacimiento: "))
nh=int(input("numero de hijos: "))
apb=int(input("años de pertenencia al banco: "))
ec=input("estado civil (c/s): ")
place=input("dondde vive (u/r): ")
an=2020-an
#here comes the pain
if apb >= 10 and nh >= 2:
    print("APROBADO")
elif ec== "c" or ec== "C" and nh >=3 and an >= 45 and an <= 55:
    print("APROBADO")
elif ingreso >= 2500000 and ec=="s" or ec== "S" and place== "u" or place== "U":
    print("APROBADO")
elif ingreso >= 3500000 and apb >=5:
    print("APROBADO")
elif place== "r" or place== "R" and ec== "c" or ec== "C" and nh <= 2:
    print("APROBADO")
else:
    print("rechazado")