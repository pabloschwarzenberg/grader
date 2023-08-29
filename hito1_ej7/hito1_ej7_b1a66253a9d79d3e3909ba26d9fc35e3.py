dia = int(input("Ingrese su dia de nacimiento: "))
mes = int(input("Ingrese su mes de nacimiento: "))

if (((int(mes == 3)) and (dia >= 21)) or (int(mes == 4) and (dia < 20))):
    print("aries")

if (((int(mes == 4)) and (dia >= 20)) or (int(mes == 5) and (dia < 21))):
    print("tauro")

if (((int(mes == 5)) and (dia >= 21)) or (int(mes == 6) and (dia < 21))):
    print("gemini")

if (((int(mes == 6)) and (dia >= 21)) or (int(mes == 7) and (dia < 23))):
    print("cancer")

if (((int(mes == 7)) and (dia >= 23)) or (int(mes == 8) and (dia < 23))):
    print("leo")

if (((int(mes == 8)) and (dia >= 23)) or (int(mes == 9) and (dia < 23))):
    print("virgo")

if (((int(mes == 9)) and (dia >= 23)) or (int(mes == 10) and (dia < 23))):
    print("libra")

if (((int(mes == 10)) and (dia >= 23)) or (int(mes == 11) and (dia < 22))):
    print("escorpio")

if (((int(mes == 11)) and (dia >= 23)) or (int(mes == 12) and (dia < 22))):
    print("sagitario")

if (((int(mes == 12)) and (dia >= 22)) or (int(mes == 1) and (dia < 20))):
    print("capricornio")

if (((int(mes == 1)) and (dia >= 20)) or (int(mes == 2) and (dia < 19))):
    print("acuario")

if (((int(mes == 2)) and (dia >= 19)) or (int(mes == 3) and (dia < 20))):
    print("piscis")