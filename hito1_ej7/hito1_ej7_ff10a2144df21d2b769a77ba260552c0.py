#Zodiaco
dia=int(input())
mes=int(input())
if (mes==3 and dia in range(21,32)) or (mes==4 and dia in range(1,21)):
    print("Aries")
if (mes==4 and dia in range(21,31)) or (mes==5 and dia in range(1,22)):
    print("Tauro")
if (mes==5 and dia in range(22,32)) or (mes==6 and dia in range(1,22)):
    print("Géminis")
if (mes==6 and dia in range(22,31)) or (mes==7 and dia in range(1,23)):
    print("Cáncer")
if (mes==7 and dia in range(23,32)) or (mes==8 and dia in range(1,23)):
    print("Leo")
if (mes==8 and dia in range(23,32)) or (mes==9 and dia in range(1,24)):
    print("Virgo")
if (mes==9 and dia in range(24,31)) or (mes==10 and dia in range(1,24)):
    print("Libra")
if (mes==10 and dia in range(24,32)) or (mes==11 and dia in range(1,23)):
    print("Escorpión")
if (mes==11 and dia in range(23,31)) or (mes==12 and dia in range(1,22)):
    print("Sagitario")
if (mes==12 and dia in range(22,32)) or (mes==1 and dia in range(1,21)):
    print("Capricornio")
if (mes==1 and dia in range(21,32)) or (mes==2 and dia in range(1,20)):
    print("Acuario")
if (mes==2 and dia in range(20,29)) or (mes==3 and dia in range(1,21)):
    print("Piscis")