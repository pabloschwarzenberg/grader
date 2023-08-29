"""
8.- Escribe un programa que reciba como parámetro el día y el mes del cumpleaños
de una persona (como números enteros) y que imprima el signo del zodíaco al que pertenece.
Para determinar las fechas de cada signo utiliza la columna Tropical Zodiac en la tabla de
fechas que aparece en este link (Wikipedia).
"""

dia = int(input("Día de su nacimiento: "))
mes = int(input("Mes de su nacimiento: "))

if mes == 1:
    if dia < 21:
        signo = "Carpricornio"
    else:
        signo = "Acuario"

if mes == 2:
    if dia < 20:
        signo = "Acuario"
    else:
        signo = "Piscis"

if mes == 3:
    if dia < 21:
        signo = "Piscis"
    else:
        signo = "Aries"
    
if mes == 4:
    if dia < 21:
        signo = "Aries"
    else:
        signo = "Tauro"

if mes == 5:
    if dia < 20:
        signo = "Tauro"
    else:
        signo = "Geminis"

if mes == 6:
    if dia < 21:
        signo = "Geminis"
    else:
        signo = "Cancer"

if mes == 7:
    if dia < 21:
        signo = "Cancer"
    else:
        signo = "Leo"

if mes == 8:
    if dia < 20:
        signo = "Leo"
    else:
        signo = "Virgo"

if mes == 9:
    if dia < 21:
        signo = "Virgo"
    else:
        signo = "Libra"

if mes == 10:
    if dia < 21:
        signo = "Libra"
    else:
        signo = "Escorpio"

if mes == 11:
    if dia < 20:
        signo = "Escorpio"
    else:
        signo = "Sagitario"

if mes == 12:
    if dia < 21:
        signo = "Sagitario"
    else:
        signo = "Capricornio"

print(signo)     