#Zodiaco
fechaCumple=int(input("Ingrese día y mes de su cumpleaños: "))
dia=fechaCumple//100
mes=fechaCumple%100
cumple=(mes*100)+dia
if cumple>=322 and cumple<=420:
    print("ARIES")
if cumple>=421 and cumple<=521:
    print("TAURO")
if cumple>=522 and cumple<=621:
    print("GEMINIS")
if cumple>=622 and cumple<=723:
    print("CÁNCER")
if cumple>724 and cumple<=823:
    print("LEO")
if cumple>=824 and cumple<=923:
    print("VIRGO")
if cumple>=924 and cumple<=1023:
    print("LIBRA")
if cumple>=1024 and cumple<=1122:
    print("ESCORPIÓN")
if cumple>=1123 and cumple<=1222:
    print("SAGITARIO")
if cumple>=1223 and cumple<=120:
    print("CAPRICORNIO")
if cumple>=121 and cumple<=219:
    print("ACUARIO")
if cumple>=220 and cumple<=321:
    print("PICIS")