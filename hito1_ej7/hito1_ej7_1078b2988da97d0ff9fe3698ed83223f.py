#Zodiaco


dia = int(input("Ingrese dia del cumpleaños: "))
mes = int(input("Ingrese mes del cumpleaños: "))

diatotal = (mes - 1)* 30 + dia

if 80 <= diatotal <= 109:
    print("Aries")
elif 110 <= diatotal <= 140:
    print("Tauro")
elif 141 <= diatotal <= 171:
    print("Geminis")
elif 172 <= diatotal <= 203:
    print("Cancer")
elif 204 <= diatotal <= 234:
    print("Leo")
elif 235 <= diatotal <= 265:
    print("Virgo")
elif 266 <= diatotal <= 295:
    print("Libra")
elif 296 <= diatotal <= 325:
    print("Escorpio")
elif 326 <= diatotal <= 355:
    print("Sagitario")
elif 356 <= diatotal <= 365:
    print("Capricornio")
elif 20 <= diatotal <= 49:
    print("Acuario")
elif 50 <= diatotal <= 79:
    print("Piscis")
else:
    print("Capricornio")
