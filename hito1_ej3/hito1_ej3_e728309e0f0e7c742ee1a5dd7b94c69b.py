ingreso = float(input('ingrese su ingreso en pesos'))
nacimiento = float(input('ingrese su ano de nacimiento'))
numerohijos = float(input('ingrese su cantidad de hijos'))
pertencia = float(input('ingrese sus anos de permanencia al banco'))
estado_civil = input('ingrese una "S": soltero o  "C", casado')
vive = input('ingrese si vive en campo o cuidad ("U": urbano, "R": rural)')
edad = 2020 - nacimiento

if pertencia > 10 and numerohijos >= 2:
    print ('APROBADO')
    
elif estado_civil == "C" and numerohijos > 3 and 55 < edad > 45:
     print ('APROBADO')

elif ingreso > 2500000 and estado_civil == "S" and vive == "u" :
    print ('APROBADO')

elif ingreso > 3500000 and pertencia > 5:
     print ('APROBADO')

elif vive == "R" and estado_civil == "C" and numerohijos < 2:
     print ('APROBADO')

else :
    print ('RECHAZADO')    