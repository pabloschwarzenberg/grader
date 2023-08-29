dia = int(input("Ingrese el día de nacimiento:"))
mes = int(input("Ingrese el mes de nacimiento:"))
if(mes >= 1 and mes <= 2):
    if((mes == 1 and dia >= 21) or (mes == 2 and dia <= 18)):
        print("acuario")
    else:
        print("piscis")
if(mes >= 3 and mes <= 4):
    if((mes == 3 and dia >= 21) or (mes == 4 and dia <= 20)):
        print("aries")
    else:
        print("tauro")
if(mes >= 5 and mes <= 6):
    if((mes == 5 and dia >= 21) or (mes == 6 and dia <= 21)):
        print("geminis")
    else:
        print("cancer")
if(mes >= 7 and mes <= 8):
    if((mes == 7 and dia >= 23) or (mes == 8 and dia <= 22)):
        print("leo")
    else:
        print("virgo")
if(mes >= 9 and mes <= 10):
    if((mes == 9 and dia >= 23) or (mes == 10 and dia <= 22)):
        print("libra")
    else:
        if(mes == 9 and dia <= 22):
            print("virgo")
        else:
            print("escorpio")
if(mes >= 11 and mes <= 12):
    if((mes == 11 and dia >= 23) or (mes == 12 and dia <= 21)):
        print("sagitario")
    else:
        print("capricornio")
if(mes == 12 or mes == 1):
    if((mes == 12 and dia >= 22) or (mes == 1 and dia <= 20)):
        print("capricornio")