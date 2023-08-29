#Zodiaco
Mes= int(input("Ingrese el numero de mes en el que nacio:")) 
Dia = int(input("Ingrese el numero del dia en que nacio:")) 
if(Dia >= 21 and Mes == 3) or (Dia <=20 and Mes ==4):
 print("Aries")
elif(Dia >= 20 and Mes == 4) or (Dia <=20 and Mes ==5):
 print("Tauro")
elif(Dia >= 21 and Mes == 5) or (Dia <=21 and Mes ==6):
 print("Geminis")
elif(Dia >= 21 and Mes == 6) or (Dia <=23 and Mes ==7):
 print("Cancer")
elif(Dia >= 23 and Mes == 7) or (Dia <=23 and Mes ==8):
 print("Leo")
elif(Dia >= 23 and Mes == 8) or (Dia <=23 and Mes ==9):
 print("Virgo")
elif(Dia >= 23 and Mes == 9) or (Dia <=23 and Mes ==10):
 print("Libra")
elif(Dia >= 23 and Mes == 10) or (Dia <=20 and Mes ==11):
 print("Escorpio")
elif(Dia >= 22 and Mes == 11) or (Dia <=22 and Mes ==12):
 print("Sagitario")
elif(Dia >= 22 and Mes == 12) or (Dia <=20 and Mes ==1):
 print("Capricornio")
elif(Dia >= 20 and Mes == 1) or (Dia <=19 and Mes ==2):
 print("Acuario")
else:
 print("Piscis")