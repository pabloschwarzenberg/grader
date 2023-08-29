#Zodiaco
dia = input("Ingresa Dia de Nacimiento")
mes = input("ingresa mes de Nacimiento")

if ((int(mes)==12 and int(dia) >= 22)or(int(mes)==1 and int(dia)<= 19)):
        signo = ("\n Capricornio")
elif ((int(mes)==1 and int(dia) >= 20)or(int(mes)==2 and int(dia)<= 17)):
        signo = ("\n Acuario")
elif ((int(mes)==2 and int(dia) >= 18)or(int(mes)==3 and int(dia)<= 19)):
        signo = ("\n Piscis")
elif ((int(mes)==3 and int(dia) >= 20)or(int(mes)==4 and int(dia)<= 19)):
        signo = ("\n Aries")
elif ((int(mes)==4 and int(dia) >= 20)or(int(mes)==5 and int(dia)<= 20)):
        signo = ("\n Tauro")
elif ((int(mes)==5 and int(dia) >= 21)or(int(mes)==6 and int(dia)<= 20)):
        signo = ("\n Geminis")
elif ((int(mes)==6 and int(dia) >= 21)or(int(mes)==7 and int(dia)<= 22)):
        signo = ("\n Cancer")
elif ((int(mes)==7 and int(dia) >= 23)or(int(mes)==8 and int(dia)<= 22)):
        signo = ("\n Leo")
elif ((int(mes)==8 and int(dia) >= 23)or(int(mes)==9 and int(dia)<= 22)):
        signo = ("\n Virgo")
elif ((int(mes)==9 and int(dia) >= 23)or(int(mes)==10 and int(dia)<= 22)):
        signo = ("\n Libra")
elif ((int(mes)==10 and int(dia) >= 23)or(int(mes)==11 and int(dia)<= 21)):
        signo = ("\n Escorpión")
elif ((int(mes)==11 and int(dia) >= 22)or(int(mes)==12 and int(dia)<= 21)):
        signo = ("\n Sagitario")


print("Tu Signo es: ",signo)