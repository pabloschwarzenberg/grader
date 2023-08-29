#Zodiaco
dia = int(input("ingrese dia en el que nacio: "))
mes = int(input("ingrese mes en el que nacio: "))
mes_lista = mes - 1

s_zodiacales = ["acuario", "piscis", "aries", "tauro", "geminis", "cancer", "leo", "virgo", "libra", "escorpio", "sagitario", "capricornio"]
#enero marzo abril mayo 21
signo = ""
if mes in [1,3,4,5]:
    if dia < 21:
        signo = s_zodiacales[mes_lista - 1]
    else:
        signo = s_zodiacales[mes_lista]
#junio diciembre 22
elif mes in [6,12]:
    if dia < 22:
        signo = s_zodiacales[mes_lista - 1]
    else:
        signo = s_zodiacales[mes_lista]
#julio septiembre octubre noviembre 23
elif mes in [7,9,10,11]:
    if dia < 23:
        signo = s_zodiacales[mes_lista - 1]
    else:
        signo = s_zodiacales[mes_lista]
#agosto 24 
elif mes in [8]:
    if dia < 24:
        signo = s_zodiacales[mes_lista - 1]
    else:
        signo = s_zodiacales[mes_lista]
#febrero 20
elif mes in [2]:
    if dia < 20:
        signo = s_zodiacales[mes_lista - 1]
    else:
        signo = s_zodiacales[mes_lista]
else:
    print("ese mes no existe")

print(signo)      