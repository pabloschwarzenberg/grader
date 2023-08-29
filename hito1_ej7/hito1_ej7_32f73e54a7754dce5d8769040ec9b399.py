#Zodiaco

dia=int(input("ingrese día:"))
mes=int(input("ingrese mes:"))
if  ((3==mes)and(21<dia))or((4==mes)and(dia<=20)):
    print("aries")
elif ((4==mes)and(20<dia))or((5==mes)and(dia<=21)):
    print("tauro")
elif ((5==mes)and(21<dia))or((6==mes)and(dia<=21)):
    print("geminis")
elif ((6==mes)and(21<dia))or((7==mes)and(dia<=23)):
    print("cancer")
elif ((7==mes)and(23<dia))or((8==mes)and(dia<=23)):
    print("leo")
elif ((8==mes)and(23<dia))or((9==mes)and(dia<=23)):
    print("virgo")
elif ((9==mes)and(23<dia))or((10==mes)and(dia<=23)):
    print("libra")
elif ((10==mes)and(23<dia))or((11==mes)and(dia<=22)):
    print("escorpio")
elif ((11==mes)and(22<dia))or((12==mes)and(dia<=22)):
    print("sagitario")
elif ((12==mes)and(22<dia))or((1==mes)and(dia<=20)):
    print("capricornio")
elif ((1==mes)and(20<dia))or((2==mes)and(dia<=19)):
    print("acuario")
elif ((2==mes)and(19<dia))or((3==mes)and(dia<=21)):
    print("piscis")
else:
    print("la fecha no es válida")