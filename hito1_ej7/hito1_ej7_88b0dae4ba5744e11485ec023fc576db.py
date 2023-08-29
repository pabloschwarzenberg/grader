#Zodiaco
dia = input("Dia: ")
mes = input("Mes: ")

if mes[0] == "0":
    mesNuevo = mes[2]
else:
    mesNuevo = mes

diaMes = eval(mesNuevo + dia)

if 120 < diaMes < 219:
    signo = "Acuario"
elif 219 < diaMes < 321:
    signo = "Piscis"
elif 321 < diaMes < 420:
    signo = "Aries"
elif 420 < diaMes < 521:
    signo = "Tauro"
elif 521 < diaMes < 621:
    signo = "Geminis"
elif 621 < diaMes < 723:
    signo = "Cancer"
elif 723 < diaMes < 823:
    signo = "Leo"
elif 823 < diaMes < 923:
    signo = "Virgo"
elif 923 < diaMes < 1023:
    signo = "Libra"
elif 1023 < diaMes < 1122:
    signo = "Escorpio"
elif 1123 < diaMes < 1222:
    signo = "Sagitario"
elif 1222 < diaMes < 1230 or 101 < diaMes < 120:
    signo = "Capricornio"

print(signo)
