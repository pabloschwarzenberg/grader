#Zodiaco
dia = int(input())
mes = int(input())

if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 20):
    print("Aries")

elif (mes == 4 and dia >= 21) or (mes == 5 and dia <= 20):
    print("Tauro")

elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
    print("Géminis")

elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 20):
    print("Cáncer")

elif (mes == 7 and dia >= 21) or (mes == 8 and dia <= 20):
    print("Leo")

elif (mes == 8 and dia >= 21) or (mes == 9 and dia <= 20):
    print("Virgo")

elif (mes == 9 and dia >= 21) or (mes == 10 and dia <= 20):
    print("Libra")

elif (mes == 10 and dia >= 21) or (mes == 11 and dia <= 20):
    print("Escorpio")

elif (mes == 11 and dia >= 21) or (mes == 12 and dia <= 20):
    print("Sagitario")

elif (mes == 12 and dia >= 21) or (mes == 1 and dia <= 20):
    print("Capricornio")

elif (mes == 1 and dia >= 21) or (mes == 2 and dia <= 20):
    print("Acuario")

else:
    print("Piscis")