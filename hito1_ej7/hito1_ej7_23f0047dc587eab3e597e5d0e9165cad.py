#Zodiaco
print("Hola, bienvenido al buscador de signo zodiacal")
print("Para saber tu signo ingresa tu día y mes de nacimiento:")

dia=(input("día:",))
mes=(input("mes con dos digitos:",))

diafc=int(dia)
mesfc=int(mes)

if(diafc>=21 and mes=="03") or (1<=diafc<=20 and mes=="04"):
    print("aries")
elif(diafc>=21 and mes=="04") or (1<=diafc<=21 and mes=="05"):
    print("tauro")
elif(diafc>=22 and mes=="05") or (1<=diafc<=21 and mes=="06"):
    print("geminis")
elif(diafc>=22 and mes=="06") or (1<=diafc<=22 and mes=="07"):
    print("cancer")
elif(diafc>=23 and mes=="07") or (1<=diafc<=22 and mes=="08"):
    print("leo")
elif(diafc>=23 and mes=="08") or (1<=diafc<=23 and mes=="09"):
    print("virgo")
elif(diafc>=24 and mes=="09") or (1<=diafc<=23 and mes=="10"):
    print("libra")
elif(diafc>=24 and mes=="10") or (1<=diafc<=22 and mes=="11"):
    print("escorpion")
elif(diafc>=23 and mes=="11") or (1<=diafc<=21 and mes=="12"):
    print("sagitario")
elif(diafc>=23 and mes=="12") or (1<=diafc<=20 and mes=="01"):
    print("capricornio")
elif(diafc>=21 and mes=="01") or (1<=diafc<=19 and mes=="02"):
    print("acuario")
elif(diafc>=20 and mes=="02") or (1<=diafc<=20 and mes=="03"):
    print("piscis")
      