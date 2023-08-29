#variables
print("----------------------------------")
dia=int(input("ingrese su día de Cumpleaños :"))
mes=int(input("ingrese su mes de Cumpleaños :"))

if(dia>=21 and mes==3)or (dia<=20 and mes==4):
    print("Aries")
elif(dia>=21 and mes==4)or (dia<=20 and mes==5):
    print("Tauro")
elif(dia>=21 and mes==5)or (dia<=20 and mes==6):
    print("geminis")
elif(dia>=21 and mes==6)or (dia<=20 and mes==7):
    print("Cáncer")
elif(dia>=21 and mes==7)or (dia<=20 and mes==8):
    print("Leo")
elif(dia>=21 and mes==8)or (dia<=20 and mes==9):
    print("Virgo")
elif(dia>=21 and mes==9)or (dia<=20 and mes==10):
    print("Libra")
elif(dia>=21 and mes==10)or (dia<=20 and mes==11):
    print("Escorpio")
elif(dia>=21 and mes==11)or (dia<=20 and mes==12):
    print("Sagitario")
elif(dia>=21 and mes==12)or (dia<=20 and mes==1):
    print("Capricornio")
elif(dia>=21 and mes==1)or (dia<=20 and mes==2):
    print("Acuario")
elif(dia>=21 and mes==2)or (dia<=20 and mes==3):
    print("Piscis")    
else:
    print("indique nuevamente sus datos")
