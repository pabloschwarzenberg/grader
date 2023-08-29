print("\nEscriba su dia y mes de cumpleanos en este formato DD/M.")
fecha = input("Ingrese aqui la fecha: ").split("/")

dia = fecha[0]
mes = fecha[1]
dia =int(dia)
mes = int(mes)



if mes == 12:
    if dia < 22:
        astro = "Sagitario"
    else:
        astro = "Capricornio"

elif mes == 1  :
    if dia < 20 :
        astro = "Capricornio  "
    else:
        astro = "Acuario "

elif mes == 2  :
    if dia < 19 :
        astro = "Acuario  "
    else:
        astro = "Piscis "

elif mes ==  3 :
    if dia < 21 :
        astro = "Piscis  "
    else:
        astro = "Aries "

elif mes ==  4 :
    if dia < 20 :
        astro = "Aries "
    else:
        astro = "Tauro "

elif mes ==  5 :
    if dia < 21 :
        astro = "Tauro  "
    else:
        astro = "Geminis "

elif mes ==  6 :
    if dia < 21 :
        astro = "Geminis "
    else:
        astro = "Cancer "

elif mes == 7  :
    if dia < 23  :
        astro = "Cancer  "
    else:
        astro = "Leo "

elif mes == 8  :
    if dia < 23 :
        astro = "Leo "
    else:
        astro = "Virgo "

elif mes ==   9:
    if dia < 23 :
        astro = "Virgo  "
    else:
        astro = "Libra "

elif mes ==   10:
    if dia < 23  :
        astro = "Libra  "
    else:
        astro = "Escorpio "

elif mes ==  11 :
    if dia < 22  :
        astro = "Escorpio  "
    else:
        astro = "Sagitario "

print(astro)
