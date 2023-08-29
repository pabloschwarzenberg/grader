#Aprobación de créditos
ing= int(input("¿cual es su ingreso en pesos?:"))
an= int(input("ingrese su año de nacimiento:"))
nh= int(input("ingrese la cantidad de hijos que tiene:"))
apb= int(input("ingrese el año de pertenencia en el banco:"))
ec= input("es usted solter(a) o casad(a):")
cc= input("usted vive en zona urbana o rural:")
edad= 2018 - an
if apb > 10 and nh >= 2:
 print("APROBADO")
elif ing > 2500000 and ec == "S"and cc == "U":
 print("APROBADO")
elif ing > 3500000 and apb > 5:
 print("APROBADO")
elif cc == "R" and ec == "U" and nh < 2:
 print("APROBADO")
elif ec == "C" and nh > 3 and (edad <= 55 and edad >= 45):
 print("APROBADO")
elif cc == "R" and ec == "C" and nh < 2:
 print("APROBADO")
else:
 print("RECHAZADO")