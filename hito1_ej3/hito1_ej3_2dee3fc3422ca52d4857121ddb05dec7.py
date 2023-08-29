while True:
    try:
        ing = int(input("Escriba sus ingresos: "))
        break
    except ValueError:
        print("Oops! No es un numero valido, intente nuevamente")
while True:
    try:
        año = int(input("Escriba el año de su nacimiento"))
        edad=2018-año
        break
    except ValueError:
        print("Oops! No es un numero valido, intente nuevamente")
while True:
    try:
        hi = int(input("Escriba el numero de hijos que tiene: "))
        break
    except ValueError:
        print("Oops! No es un numero valido, intente nuevamente")
while True:
    try:
        pm = int(input("Escriba los años de permanencia que tiene con el banco: "))
        break
    except ValueError:
        print("Oops! No es un numero valido, intente nuevamente")
while True:
    eC = str(input("Escriba su estado civil, S para soltero y C para casado: "))
    if not(eC.isalpha()):
        eC = str(input("Debe solamente ser letras y no combinaciones numericas: "))
        break
    break
while True:
    v = str(input("Escriba su lugar de vivienda, U para urbano y R para rural: "))
    if not(v.isalpha()):
         v = str(input("Debe solamente ser letras y no combinaciones numericas: "))
         break
    break
if(pm>10 and hi>=2):
    print("APROBADO")
elif(eC=="C" and hi>3 and 55>=edad>=45):
    print("APROBADO")
elif(ing>2500000 and eC=="S" and v=="U"):
    print("APROBADO")
elif(ing>3500000 and pm>5):
    print("APROBADO")
elif(v=="R" and eC=="C" and hi<2):
    print("APROBADO")
else:
    print("RECHAZADO")