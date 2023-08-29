#Zodiaco
dia=int(input("Ingrese dia de nacimiento: "))
mes=int(input("Ingrese mes de nacimiento: "))

if((mes==3) and (dia >= 21 )) or ((mes== 4) and (dia<=20)):
   print("signo: Aries")
if((mes==4) and (dia >= 21)) or ((mes== 5) and (dia<=20)):
   print("signo:Tauro")
if((mes==5) and (dia >= 21)) or ((mes== 6) and (dia<=21)):
   print("signo:Geminis")
if((mes==6) and (dia >= 22)) or ((mes== 7) and (dia<=22)):
   print("signo:Cancer")
if((mes==7) and (dia >=23)) or ((mes==8) and (dia<=22)):
   print("signo:Leo")
if((mes==8) and (dia >= 23)) or ((mes== 9) and (dia<=22)):
   print("signo:Virgo")
if((mes==9) and (dia >= 23)) or ((mes== 10) and (dia<=22)):
   print("signo:Libra")
if((mes==10) and (dia >= 23)) or ((mes==11) and (dia<=22)):
   print("Signo:Escorpio")
if((mes==11) and (dia >=23)) or ((mes==12)and (dia<=21)):
   print("signo:Sagitario")
if((mes==12) and (dia>=22)) or ((mes==1) and (dia<=20)):
   print("signo:Capricornio")
if((mes==1) and (dia>=21)) or ((mes==2) and (dia<=18)):
   print("signo:Acuario")
if((mes==2) and (dia>=19)) or ((mes==3) and (dia<=20)):
   print("signo:Piscis")