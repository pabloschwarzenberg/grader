#Zodiaco
dia=int(input("ingrese dia de nacimiento: "))
mes=int(input("ingrese mes de nacimiento: "))

ndia=((mes-1)*30)+dia


if ndia>=80 and ndia<=110:
    print("aries")
elif ndia>=111 and ndia <= 141:
    print("tauro")
elif ndia>=142 and ndia<=172:
    print("géminis")
elif ndia>=173 and ndia<=204:
    print("cáncer")
elif ndia>=205 and ndia<=235:
    print("leo")
elif ndia>=236 and ndia<=265:
    print("virgo")
elif ndia>=266 and ndia<=295:
    print("libra")
elif ndia>=296 and ndia<=326:
    print("escorpio")
elif ndia>=327 and ndia<=355:
    print("sagitario")
elif (ndia>=355 and ndia <=365) or (ndia>=1 and ndia<=19):
    print("capricornio")
elif ndia>=20 and ndia<=49:
    print("acuario")
elif ndia>=50 and ndia<=79:
    print("piscis")
else:
    print("ERROR: ingresa una fecha valida")