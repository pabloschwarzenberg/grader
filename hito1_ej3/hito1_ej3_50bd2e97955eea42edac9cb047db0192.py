a = eval(input("ingreso :"))
b = eval(input("ano de nacimiento:"))
c = eval(input("numero de hijos :"))
d = eval(input("anos de pertenencia al banco :"))
e = str(input("estado civil :"))
f = str(input("Urbano o Rural :"))
 

if (a >2500000) and (e=="S") and (f=="U"):
    print("APROBADO")

elif (d>10) and (c >=2):
    print("APROBADO")

elif (e=="C") and (c >3) and (b>45) and (b<55):
    print("APROBADO")

elif (a >3500000) and (d>5):
    print("APROBADO")

elif (f=="R") and (e=="C") and (c<2):
    print("APROBADO")
    
else:
    print ("RECHAZADO")

