#Aprobación de créditos
ingreso=int(input("ingrese su ingreso en pesos:"))
nacimiento=int(input("ingrese su año de nacimiento:"))
numerohijos=int(input("ingrese el numero de sus hijos:"))
añospertenencia=int(input("ingrese la cantidad de años en el banco:"))
estadocivil= str(input("ingrese su estado civil:"))
dondevive=str(input("ingrese si vive en urbano o rural:"))
edad=2020-nacimiento
if (añospertenencia>10) and (numerohijos>=2):
    print("credito APROBADO")

elif(estadocivil== "C")and(numerohijos>3)and (45>=edad<=55):
    print("credito APROBADO")

elif (ingreso>2500000) and (estadocivil== "S") and (dondevive== "U"):
    print("credito APROBADO")

elif (ingreso>3500000)and (añospertenencia>5):
    print("credito APROBADO")

elif (dondevive== "R")and(estadocivil=="C")and(numerohijos<2):
    print("credito APROBADO")
else:
     print("credito RECHAZADO")      