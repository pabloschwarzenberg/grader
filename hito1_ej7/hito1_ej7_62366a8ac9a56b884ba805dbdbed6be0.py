#Zodiaco
# Entrada

dia = int(input("Escriba su dia de nacimiento: "))
mes = int(input("Escriba su mes de nacimiento: "))

# procesamiento
if 1 <= dia <= 31 and 1 <= mes <= 12:
# Aries
    if dia >= 22 and mes == 3 or dia <= 20 and mes == 4:
        print("aries")
# Tauro
    if dia >= 21 and mes == 4 or dia <= 21 and mes == 5:
        print("tauro")
# Geminis
    if dia >= 22 and mes == 5 or dia <= 21 and mes == 6:
        print("geminis")
# Cancer
    if dia >= 22 and mes == 6 or dia <= 23 and mes == 7:
        print("cancer")
# Leo
    if dia >= 24 and mes == 7 or dia <= 23 and mes == 8:
        print("leo")
# Virgo
    if dia >= 24 and mes == 8 or dia <= 23 and mes == 9:
        print("virgo")
# Libra
    if dia >= 24 and mes == 9 or dia <= 23 and mes == 10:
        print("libra")
# Scorpio
    if dia >= 24 and mes == 10 or dia <= 22 and mes == 11:
        print("escorpio")
# Sagitario
    if dia >= 23 and mes == 11 or dia <= 22 and mes == 12:
        print("sagitario")
# Capricornio
    if dia >= 23 and mes == 12 or dia <= 20 and mes == 1:
        print("caprocornio")
# Aquario
    if dia >= 21 and mes == 1 or dia <= 19 and mes == 2:
        print("aquario")
# Pisis
    if dia >= 20 and mes == 2 or dia <= 21 and mes == 3:
        print("pisis")
else:
    print("Mes o dia invalido")