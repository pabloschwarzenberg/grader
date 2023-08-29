print("diremos tu signo del zodiaco con tan solo tu dia y mes de nacimiento")
nombre=input("por favor ingrese su nombre: ")
 dia=int(input(" por favor ingrese su dia de nacimiento: "))
 mes=int(input("por favor ingrese su mes de nacimiento: "))
if dia>=21 and mes== 3 or dia<=20 and mes==4:
    print(nombre,"usted es Aries")
if dia>=21 and mes==4 or dia<=20 and mes==5:
    print(nombre,"usted es Tauro")
if dia>=22 and mes==5 or dia<=21 and mes==6:
    print(nombre,"usted es Geminis")
if dia>=22 and mes==6 or dia<=22 and mes==7:
    print(nombre,"usted es Cáncer")
if dia>=23 and mes==7 or dia<=23 and mes==8:
    print(nombre,"usted es Leo")
if dia>=24 and mes==8 or dia<=23 and mes==9:
    print(nombre,"usted es Virgo")
if dia>=24 and mes==9 or dia<=23 and mes==10:
    print(nombre,"usted es Libra")
if dia>=24 and mes==10 or dia<=22 and mes==11:
    print(nombre,"usted es Escorpión")
if dia>=23 and mes==11 or dia<=21 and mes==12:
    print(nombre,"usted es Sagitario")
if dia>=22 and mes==12 or dia<=20 and mes==1:
    print(nombre,"usted es Capricornio")
if dia>=21 and mes==1 or dia<=18 and mes==2:
    print(nombre,"usted es Acuario")
if dia>=19 and mes ==2 or dia<=20 and mes==3:
    print(nombre,"usted es Piscis")