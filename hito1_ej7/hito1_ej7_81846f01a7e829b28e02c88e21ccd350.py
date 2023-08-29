#Zodiaco
 dia = int(input("ingrese el numero del dia que nacio [1-31]: "))
while not (dia>=1 and dia<=31):
    dia= int(input("ERROR.... no pertenece a ningun dia ingrese [1-31]"))
mes = int(input("ingrese el numero del mes que nacio [1-12]: "))
while not (mes>=1 and mes<=12):
    mes= int(input("ERROR.... no pertenece a ningun mes ingrese [1-12]")) 
if dia>=22 and dia<=31 and mes==12:
    print ("capricornio")
elif dia>=1 and dia <=21 and mes==1:
    print ("capricornio")
elif dia>=21 and dia<=18 and mes>=1 and mes<=2:
    print ("acuario")
elif dia>=19 and dia<=20 and mes>=2 and mes<=3:
    print ("piscis")
elif dia>=21 and dia<=20 and mes>=3 and mes<=4:
    print ("aries")
elif dia>=21 and dia<=20 and mes>=4 and mes<=5:
    print ("tauro")
elif dia>=21 and dia<=21 and mes>=5 and mes<=6:
    print ("geminis")
elif dia>=22 and dia<=22 and mes>=6 and mes<=7:
    print ("cancer")
elif dia>=23 and dia<=22 and mes>=7 and mes<=8:
    print ("leo")
elif dia>=23 and dia<=22 and mes>=8 and mes<=9:
    print ("virgo")
elif dia>=23 and dia<=22 and mes>=9 and mes<=10:
    print ("libra")
elif dia>=23 and dia<=22 and mes>=10 and mes<=11:
    print ("escorpio")
elif dia>=23 and dia<=21 and mes>=11 and mes<=12:
    print ("sagitario")
     