#Zodiaco
Fecha = eval(input("ingrese fecha de nacimiento(dd en numero entero): "))
Mes = eval(input("ingrese el mes de nacimiento(m en numero entero): "))
print("fecha de nacimiento:{}/{} ".format(Fecha , Mes))
if(Mes == 1 and Fecha <= 20) or (Mes == 12 and Fecha >= 23):
    print("usted es Capricornio")
if(Mes == 1 and Fecha >= 21) or (Mes == 2 and Fecha <= 19):
    print("usted es Acuario")
if(Mes == 2 and Fecha >= 20) or (Mes == 3 and Fecha <= 21):
    print("Usted es piscis")
if(Mes == 3 and Fecha >= 22) or (Mes == 4 and Fecha <= 21):
    print("Usted es aries")
if(Mes == 4 and Fecha >= 22) or (Mes == 5 and Fecha <= 21):
    print("Usted es Tauro")
if(Mes == 5 and Fecha >= 22) or (Mes == 6 and Fecha <= 21):
    print("Usted es Geminis")
if(Mes == 6 and Fecha >= 22) or (Mes == 7 and Fecha <= 23):
    print("Usted es Cancer")
if(Mes == 7 and Fecha >= 24) or (Mes == 8 and Fecha <= 23):
    print("Usted es Leo")
if(Mes == 8 and Fecha >= 24) or (Mes == 9 and Fecha <= 23):
    print("Usted es Virgo")
if(Mes == 9 and Fecha >= 24) or (Mes == 10 and Fecha <= 23):
    print("Usted es Libra")
if(Mes == 10 and Fecha >= 24) or (Mes == 11 and Fecha <= 22):
    print("Usted es Escorpio")
if(Mes == 11 and Fecha >= 23) or (Mes == 12 and Fecha <= 22):
    print("Usted es Sagitario")