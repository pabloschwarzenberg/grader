#Zodiaco
a=int(input("ingresa el dia de tu cumpleaños: "))
x=int(input("ingresa el numero del mes de tu cumpleaños: "))

if x==1:
    z=0
elif x==2:
    z=31
elif x==3:
    z=59
elif x==4:
    z=90
elif x==5:
    z=120
elif x==6:
    z=151
elif x==7:
    z=181
elif x==8:
    z=212
elif x==9:
    z=243
elif x==10:
    z=273
elif x==11:
    z=304
else:
    z=334

n=z+a

if n<=20 or n>=356:
    print("capricornio")
elif 21<=n<=50:
    print("acuario")
elif 51<=n<=79:
    print("piscis")
elif 80<=n<=110:
    print("aries")
elif 111<=n<=141:
    print("tauro")
elif 142<=n<=172:
    print("geminis")
elif 173<=n<=203:
    print("cancer")
elif 204<=n<=234:
    print("leo")
elif 235<=n<=266:
    print("virgo")
elif 267<=n<=296:
    print("escorpion")
else:
    print("sagitario")     