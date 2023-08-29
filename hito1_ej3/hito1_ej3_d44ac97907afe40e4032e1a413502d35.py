#Aprobación de créditos
ingreso = int(input("Digite su ingreso: "))
año = int(input("Indique su año de nacimiento: "))
hijos = eval(input("Indique cuantos hijos tiene: "))
pertBanco = eval(input("Indique años de pertenencia en este banco: "))
estado = input("Ingrese su estado civil (si está soltero una S, si está casado una C): ")
zona = input("Ingrese la zona en la que vive (Si vive en zona rural R, si es urbana U): ")
ap = "APROBADO"
re = "RECHAZADO"
if (pertBanco > 10) and (hijos >= 2):
    print(ap)
elif (estado == "C") or (estado == "c") and (hijos>3) and (año >=1965 and año <= 1975):
    print(ap)
elif (ingreso >= 2500000) and estado == "S" or estado == "s" and zona == "U" or zona== "u":
    print(ap)
elif (ingreso >= 3500000) and (pertBanco > 5):
    print(ap)              
elif (zona == "U") or (zona == "u") and (estado == "C") or (estado == "c") and (hijos < 2):
    print(ap)
else:
    print(re)   