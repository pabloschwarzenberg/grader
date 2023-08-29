# Algoritmo para obtener signo zodiacal.

dia_nacimiento = int(input("Ingrese dia de nacimiento : "))
mes_nacimiento = int(input("Ingrese mes de nacimiento : "))

# Transforma valores.
mes_dia = int(("00"+str(mes_nacimiento))[-2:] + ("00"+str(dia_nacimiento))[-2:])

# Diccionario con zodiaco.
zodiaco = {
    1222: "capricornio",
    1122: "sagitario",
    1023: "escorpio",
    923: "libra",
    823: "virgo",
    723: "leo",
    621: "cancer",
    521: "geminis",
    420: "tauro",
    321: "aries",
    219: "piscis",
    120: "acuario",
    0: "capricornio"
}

# Diccionario con zodiaco.
for i in zodiaco:
    if mes_dia >= i:
        print(" "+zodiaco[i])
        break
