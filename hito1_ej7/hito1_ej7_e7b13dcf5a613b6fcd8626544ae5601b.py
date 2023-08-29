#Zodiaco
def signo(dia, mes):
    if(mes == 3):
        if(dia >= 21 and dia <=31):
            print("Aries")
            return ""
        else:
            print("Piscis")
            return ""
    elif(mes == 4):
        if(dia >=1 and dia <=20):
            print("Aries")
            return ""
        else:
            print("Tauro")
            return ""
    elif(mes == 5):
        if(dia >=1 and dia <=21):
            print("Tauro")
            return ""
        else:
            print("Gemini")
            return ""
    elif(mes == 6):
        if(dia >=1 and dia <=21):
            print("Gemini")
            return ""
        else:
            print("Cancer")
            return ""
    elif(mes == 7):
        if(dia >=1 and dia <=22):
            print("Cancer")
            return ""
        else:
            print("Leo")
            return ""
    elif(mes == 8):
        if(dia >=1 and dia <=22):
            print("Leo")
            return ""
        else:
            print("Virgo")
            return ""
    elif(mes == 9):
        if(dia >=1 and dia <=23):
            print("Virgo")
            return ""
        else:
            print("Libra")
            return ""
    elif(mes == 10):
        if(dia >=1 and dia <=23):
            print("Libra")
            return ""
        else:
            print("Escorpio")
            return ""
    elif(mes == 11):
        if(dia >=1 and dia <=22):
            print("Escorpio")
            return ""
        else:
            print("Sagitario")
            return ""
    elif(mes == 12):
        if(dia >=1 and dia <=21):
            print("Sagitario")
            return ""
        else:
            print("Capricornio")
            return ""
    elif(mes == 1):
        if(dia >=1 and dia <=20):
            print("Capricornio")
            return ""
        else:
            print("Acuario")
            return ""
    elif(mes == 2):
        if(dia >=1 and dia <=19):
            print("Acuario")
            return ""
        else:
            print("Piscis")
            return ""

dia = int(input("Ingrese su dia de nacimiento: "))
mes = int(input("Ingrese su mes de nacimiento: "))
signo(dia, mes)      