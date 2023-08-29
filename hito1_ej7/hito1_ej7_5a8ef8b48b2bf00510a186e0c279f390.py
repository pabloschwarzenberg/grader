#Encabezado y solicitud de informacion por teclado
dia = int(input("Ingrese día de nacimiento: "))
mes = int(input("Ingrese mes de nacimiento: "))


#Aries 21 March – 20 April
if dia >= 21 and mes == 3 or dia <=20 and mes ==4:
        print("Aries")
#Tauro 20 April – 21 May
if dia >= 20 and mes == 4 or dia <=21 and mes ==5:
        print("Tauro")
#Geminis 21 May – 21 June
if dia >= 21 and mes == 5 or dia <=21 and mes ==6:
        print("Geminis")
#Cancer 21 June – 23 July
if dia >= 21 and mes == 6 or dia <=23 and mes ==7:
        print("Cancer")
#El mejor SIGNO 23 July – 23 August
if dia >= 23 and mes == 7 or dia <=23 and mes ==8:
        print("Leo")
#Virgo 23 August – 23 September
if dia >= 23 and mes == 8 or dia <=23 and mes ==9:
        print("Virgo")
#Libra 23 September – 23 October
if dia >= 23 and mes == 9 or dia <=23 and mes ==10:
        print("Libra")
#Escorpio 23 October – 22 November
if dia >= 23 and mes == 10 or dia <=22 and mes ==11:
        print("Escorpion")
#Sagitario 23 November – 22 December
if dia >= 23 and mes == 11 or dia <=22 and mes ==12:
        print("Sagitario")
#Capricornio 22 December – 20 January
if dia >= 22 and mes == 12 or dia <=20 and mes ==1:
        print("Capricornio")
#Acuario 20 January – 19 February
if dia >= 20 and mes == 1 or dia <=19 and mes ==2:
        print("Acuario")
#Picis 19 February – 21 March 
if dia >= 19 and mes == 2 or dia <=21 and mes ==3:
        print("Picis")
print("FIN.")