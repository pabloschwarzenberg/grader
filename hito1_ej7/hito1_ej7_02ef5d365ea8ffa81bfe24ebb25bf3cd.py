dia = int(input("Ingrese el día de su cumpleaños: "))
mes = int(input("Ingrese el mes de su cumpleaños: "))

diasMes = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
diasSignos = [80, 111, 142, 173, 204, 235, 267, 297, 327, 356, 21, 51]
signos = ['Aries', 'Tauro', 'Geminis', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Escorpio', 'Sagitario', 'Capricornio', 'Acuario', 'Piscis']

diaAno = diasMes[mes-1] + dia

if diasSignos[0] <= diaAno < diasSignos[1]:
    print(signos[0])
elif diasSignos[1] <= diaAno < diasSignos[2]:
    print(signos[1])
elif diasSignos[2] <= diaAno < diasSignos[3]:
    print(signos[2])
elif diasSignos[3] <= diaAno < diasSignos[4]:
    print(signos[3])
elif diasSignos[4] <= diaAno < diasSignos[5]:
    print(signos[4])
elif diasSignos[5] <= diaAno < diasSignos[6]:
    print(signos[5])
elif diasSignos[6] <= diaAno < diasSignos[7]:
    print(signos[6])
elif diasSignos[7] <= diaAno < diasSignos[8]:
    print(signos[7])
elif diasSignos[8] <= diaAno < diasSignos[9]:
    print(signos[8])
elif diasSignos[9] <= diaAno <= 365 or 1 <= diaAno < diasSignos[10]:
    print(signos[9])
elif diasSignos[10] <= diaAno < diasSignos[11]:
    print(signos[10])
elif diasSignos[11] <= diaAno < diasSignos[12]:
    print(signos[11])

print("")
