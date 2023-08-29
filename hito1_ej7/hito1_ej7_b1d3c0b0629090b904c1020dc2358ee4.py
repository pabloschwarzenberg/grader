#Zodiaco
n = (input("Ingrese su fecha de cumpleaños:"))

#Funcion para separar el string que entra en "n"
dia,mes = n.split()

#variable solo para comparar fechas.
if int(dia) < 10 :
    dia = "0"+dia
cumple = mes+dia 
cumple = int(cumple)
print(cumple)
if 321 < cumple < 420:
    print("Tu signo es ARIES")
if 421 < cumple < 520:
    print("Tu signo es TAURO")
if 521 < cumple < 621:
    print("Tu signo es GEMINIS")
if 622 < cumple < 722:
    print("Tu signo es CANCER")
if 723 < cumple < 822:
    print("Tu signo es LEO")
if 823 < cumple < 922:
    print("Tu signo es VIRGO")
if 923 < cumple < 1022:
    print("Tu signo es LIBRA")
if 1023 < cumple < 1122:
    print("Tu signo es ESCORPION")
if 1123 < cumple < 1221:
    print("Tu signo es SAGITARIO")
if 1222 < cumple < 1231 or 11 < cumple < 120:
    print("Tu signo es CAPRICORNIO")
if 121 < cumple < 218:
    print("Tu signo es ACUARIO")
if 219 < cumple < 320:
    print("Tu signo es PISCIS")
 