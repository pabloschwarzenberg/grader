ingreso = eval(input("ingrese su ingreso monetario mensual: "))

nacimiento =  eval(input("ingrese su año de nacimiento: "))
                   

hijos = eval(input("ingrese el número de hijos que tiene: "))

anosbanco = eval(input("ingrese los años que lleva junto a nuestro banco: "))
ec = str(input("ingrese C si es casado o S si es soltero:"))

cor = str(input("ingrese U si vive en ciudad o R si vive en el campo:"))





if(anosbanco > 10 and hijos >= 2):
    print("APROBADO")

elif( str(ec[-1]) == "C"  and hijos > 3 and 45 <= (2021- nacimiento) <= 55):
    print("APROBADO")
elif ( ingreso > 2500000 and str(ec[-1]) == "S"  and str(cor[-1]) == "U"):
    print("APROBADO")
elif( ingreso > 3500000 and anosbanco > 5):
    print("APROBADO")
elif ( str(cor[-1]) == "R" and str(ec[-1]) == "C" and hijos < 2):
    print("APROBADO")

else:
    print("RECHAZADO")
               