#Zodiaco
def zodiaco(d,m):
    if (21<d<=30 and m == 3) or (1<=d<=20 and m == 4):
        Aries = "Aries"
        return Aries 
    if (20<d<=30 and m == 4) or (1<=d<=21 and m == 5):
        Tauro = "Tauro"
        return Tauro 
    if (21<d<=30 and m == 5) or (1<=d<=21 and m == 6):
        Geminis = "Geminis"
        return Geminis   
    if (21<d<=30 and m == 6) or (1<=d<=23 and m == 7):
        Cancer = "Cancer"
        return Cancer
    if (23<d<=30 and m == 7) or (1<=d<=23 and m == 8):
        Leo = "Leo"
        return Leo
    if (23<d<=30 and m == 8) or (1<=d<=23 and m == 9):
        Virgo = "Virgo"
        return Virgo
    if (23<d<=30 and m == 9) or (1<=d<=23 and m == 10):
        Libra = "Libra"
        return Libra
    if (23<d<=30 and m == 10) or (1<=d<=23 and m == 11):
        Escorpio = "Escorpio"
        return Escorpio
    if (23<d<=30 and m == 11) or (1<=d<=22 and m == 12):
        Sagitario = "Sagitario"
        return Sagitario
    if (22<d<=30 and m == 12) or (1<=d<=20 and m == 1):
        Capricornio = "Capricornio"
        return Capricornio
    if (22<d<=30 and m == 1) or (1<=d<=19 and m == 2):
        Aquario = "Aquario"
        return Aquario
    if (19<d<=30 and m == 2) or (1<=d<=21 and m == 3):
        Piscis = "Piscis"
        return Piscis
dia = int(input("Ingrese dia de nacimiento: "))
mes = int(input("Ingrese mes de nacimiento: "))
print(zodiaco(dia,mes))