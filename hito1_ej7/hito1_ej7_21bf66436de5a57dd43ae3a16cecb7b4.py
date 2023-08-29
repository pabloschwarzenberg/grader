#Zodiaco
dia = int(input("Ingrese su dia de nacimiento: "))
mes = int(input("Ingrese su mes de nacimiento: "))
if mes > 12 or mes == 0:
    print("Error ingrese un mes valido")
else: 
    if dia >= 21 and mes == 3:
        print("Aries")
    elif 0<=dia<=20 and mes == 4:
        print("Aries")
    elif dia>=20 and mes == 4:
        print("Tauro")
    elif 0<=dia<=21 and mes == 5:
        print("Tauro")
    elif dia >= 21 and mes == 5:
        print("Geminis")
    elif 0<=dia<=21 and mes == 6:
        print("Geminis")
    elif dia >= 21 and mes == 6:
        print("Cancer")
    elif 0<=dia<=23 and mes == 7:
        print("Cancer")
    elif dia >= 23 and mes == 7:
         print("Leo")
    elif 0<=dia<=23 and mes == 8:
        print("Leo")
    elif dia >= 23 and mes == 8:
         print("Virgo")
    elif 0<=dia<=23 and mes == 9:
        print("Virgo")    
    elif dia >= 23 and mes == 9:
         print("Libra")
    elif 0<=dia<=23 and mes == 10:
        print("Libra")
    elif dia >= 23 and mes == 10:
         print("Escorpio")
    elif 0<=dia<=22 and mes == 11:
        print("Escorpio")
    elif dia >= 23 and mes == 11:
         print("Sagitario")
    elif 0<=dia<=22 and mes == 12:
        print("Sagitario")
    elif dia >= 22 and mes == 12:
          print("Capricornio")
    elif 0<=dia<=20 and mes == 1:
         print("Capricornio")
    elif dia >= 20 and mes == 1:
         print("Acuario")
    elif 0<=dia<=19 and mes == 2:
        print("Acuario")
    elif dia >= 19 and mes == 2:
         print("Piscis")
    elif 0<=dia<=21 and mes == 3:
        print("Piscis")