#Zodiaco
n = (input("Ingrese su fecha de cumpleaños:"))

dia = n[0:2]
mes = n[2:4]
#variable solo para comparar fechas.

cumple = mes+"/"+dia

if "3/21" < cumple < "4/20" :
    print("Tu signo es ARIES")
if "4/21" < cumple < "5/20":
    print("Tu signo es TAURO")
if "5/21" < cumple < "6/21":
    print("Tu signo es GEMINIS")
if "6/22" < cumple < "7/22":
    print("Tu signo es CANCER")
if "7/23" < cumple < "8/22":
    print("Tu signo es LEO")
if "8/23" < cumple < "9/22":
    print("Tu signo es VIRGO")
if "9/23" < cumple < "10/22":
    print("Tu signo es LIBRA")
if "10/23" < cumple < "11/22":
    print("Tu signo es ESCORPION")
if "11/23" < cumple < "12/21":
    print("Tu signo es SAGITARIO")
if "12/22" < cumple < "01/20":
    print("Tu signo es CAPRICORNIO")
if "1/21" < cumple < "2/18":
    print("Tu signo es ACUARIO")
if "2/19" < cumple < "3/20":
    print("Tu signo es PISCIS")