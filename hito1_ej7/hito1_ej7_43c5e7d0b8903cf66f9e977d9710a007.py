#Zodiaco
print("Meses dados del 1 al 12, 1=Enero,2=Feb,3=Marzo,4=Abril,5=Mayo,6=Junio")
print("7=Julio,8=Agosto,9=Septiembre,10=Octubre,11=Noviembre,12=Diciembre")
print("Ingrese dia de nacimiento: ")
dia=int(input())
print("Ingrese mes de nacimiento, desde el 1 al 12: ")
mes=int(input())


if (mes==3 and 21<=dia<=31 or mes==4 and 1<=dia<=20):
 print("Su signo del Zodiaco es Aries")

elif (mes==4 and 20<=dia<=30 or mes==5 and 1<=dia<=21):
 print("Su signo del Zodiaco es Tauro")

elif (mes==5 and 21<=dia<=31 or mes==6 and 1<dia<=21):
 print("Su signo del Zodiaco es Gemenis")

elif (mes==6 and 21<=dia<=30 or mes==7 and 1<=dia<=23):
 print("Su signo del Zodiaco es Cancer")

elif (mes==7 and 23<=dia<=31 or mes==8 and 1<=dia<=23):
 print("Su signo del Zodiaco es Leon")
                
elif (mes==8 and 23<=dia<=31 or mes==9 and 1<=dia<=23):
 print("Su signo zodiacal es Virgo")
                    
elif (mes==9 and 23<=dia<=30 or mes==10 and 1<=dia<=23):
 print("Su signo Zodiacal es Libra")
                        
elif (mes==10 and 23<=dia<=31 or mes==11 and 1<=dia<=22):
 print("Su signo Zodiacal es Escorpion")

elif (mes==11 and 22<=dia<=30 or mes==12 and 1<=dia<=22):
 print("Su signo Zodiacal es Sagitario")

elif (mes==12 and 22<=dia<=31 or mes==1 and 1<=dia<=20):
 print("Su signo Zodiacal es Capricornio")

elif (mes==1 and 20<=dia<=31 or mes==2 and 1<=dia<=19):
 print("Su signo Zodiacal es Acuario")

elif (mes==2 and 19<=dia<=29 or mes==3 and 1<=dia<=21):
 print("Su signo Zodiacal es Piscis")

