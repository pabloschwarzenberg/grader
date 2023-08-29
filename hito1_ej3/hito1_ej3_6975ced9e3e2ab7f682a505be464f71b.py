#Aprobación de créditos
i=int(input("ingreso:" ))
a=int(input("año de nacimiento: "))
h=int(input("cantidad de hijos:" ))
añ=int(input("años de pertenencia al banco: "))
es=input("ingrese estado civil, S si es soltero y C si es casado: ")
v=(input("ingrese vivienda, U si vive en urbano y R si es rural: "))
años=2017-a
if añ>10 and h>=2:
    print("APROBADO")
elif es=="C" and h>3 and 45<años<55:
    print("APROBADO")
elif i>2500000 and es=="S" and v=="U":
    print("APROBADO")
elif i>3500000 and añ>5:
    print("APROBADO")
elif h<2 and es=="C" and v=="R":
    print("APROBADO")
else: print ("REPROBADO")