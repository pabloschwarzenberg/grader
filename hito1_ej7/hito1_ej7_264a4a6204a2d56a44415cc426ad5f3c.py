#Zodiaco
dia = int(input("Por favor, ingrese el dia de su cumpleaños: "))
mes = int(input("Por favor, ingrese el mes en que cae de su cumpleaños: "))

if(dia >= 22 and mes == 12) or (dia <= 20 and mes == 1):
    print("Usted es Capricornio")
elif(dia >= 21 and mes == 1) or (dia <= 19 and mes == 2):
    print("Usted es Acuario")
elif(dia >= 20 and mes == 2) or (dia <= 20 and mes == 3):
    print("Usted es Piscis")
elif(dia >= 21 and mes == 3) or (dia <= 20 and mes == 4):
    print("Usted es Aries")
elif(dia >= 21 and mes == 4) or (dia <= 21 and mes == 5):
    print("Usted es Tauro")
elif(dia >= 22 and mes == 5) or (dia <= 21 and mes == 6):
    print("Usted es Géminis")
elif(dia >= 22 and mes == 6) or (dia <= 23 and mes == 7):
    print("Usted es Cánser")
elif(dia >= 24 and mes == 7) or (dia <= 20 and mes == 8):
    print("Usted es Leo")
elif(dia >= 24 and mes == 8) or (dia <= 23 and mes == 9):
    print("Usted es Virgo")
elif(dia >= 24 and mes == 9) or (dia <= 23 and mes == 10):
    print("Usted es Libra")
elif(dia >= 24 and mes == 10) or (dia <= 22 and mes == 11):
    print("Usted es Escorpio")
elif(dia >= 23 and mes == 11) or (dia <= 21 and mes == 12):
    print("Usted es Sagitario")