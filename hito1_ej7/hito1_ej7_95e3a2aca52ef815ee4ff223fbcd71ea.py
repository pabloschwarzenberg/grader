#Zodiaco
dia=int(input("Ingrese el día de su cumpleaños: "))
mes=int(input("Ingrese el mes de su cumpleaños: "))

if mes==1:
    n = dia

elif mes==2:
    n = dia+31

elif mes==3:
    n = dia+59

elif mes==4:
    n = dia+90

elif mes==5:
    n = dia+120

elif mes==6:
    n = dia+151

elif mes==7:
    n = dia+181

elif mes==8:
    n = dia+212

elif mes==9:
    n = dia+243

elif mes==10:
    n = dia+273

elif mes==11:
    n = dia+304

elif mes==12:
    n = dia+334

#Ahora se define el signo del zodíaco

if n<=20 and n>=356:
    print("Capricornio")

elif 21<=n<=50:
    print("Acuario")

elif 51<=n<=79:
    print("Piscis")

elif 80<=n<=110:
    print("Aries")

elif 111<=n<=141:
    print("Tauro")

elif 142<=n<=172:
    print("Géminis")

elif 173<=n<=203:
    print("Cáncer")

elif 204<=n<=234:
    print("Leo")

elif 235<=n<=266:
    print("Virgo")

elif 267<=n<=296:
    print("Libra")

elif 297<=n<=326:
    print("Escorpión")

elif 327<=n<=355:
    print("Sagitario")