#signo zodiacal
#Zodiaco
d=int(input("introduce tu dia de nacimiento: "))
m=int(input("introduce tu mes de nacimiento 1-12: "))
if(d>=21 and m==3) or (d<=20 and m==4):
    print("aries")
elif(d>=21 and m==4) or (d<=21 and m==5):
    print("tauro")
elif(d>=22 and m==5) or (d<=21 and m==6):
    print("geminis")
elif(d>=22 and m==6) or (d<=22 and m==7):
    print("cancer")
elif(d>=23 and m==7) or (d<=23 and m==8):
    print("leo")
elif(d>=24 and m==8) or (d<=23 and m==9):
    print("virgo")
elif(d>=24 and m==9) or (d<=23 and m==10):
    print("libra")
elif(d>=24 and m==10) or (d<=22 and m==11):
    print("escorpio")
elif(d>=23 and m==11) or (d<=21 and m==12):
    print("sagitario")
elif(d>=22 and m==12) or (d<=20 and m==1):
    print("capricornio")
elif(d>=21 and m==1) or (d<=18 and m==2):
    print("acuario")
elif(d>=19 and m==2) or (d<=20 and m==3):
    print("piscis")
#Descomponer un número
Number=int(input("ingrese cualquier número natural de 1,2,3 o 4 cifras:"))

if 0<Number<10000:

  mil = Number//1000

  centena = (Number%1000)//100

  decena = ((Number%1000)%100)//10

  unidad = ((Number%1000)%100)%10

  print(str(mil)+"M + "+str(centena)+"C + "+str(decena)+"D + "+str(unidad)+"U")

else:

  print("un numéro con un máximo de 4 digitos")