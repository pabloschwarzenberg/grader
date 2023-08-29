#Entradas
día = int(input("Ingrese su día de cumpleaños: "))
mes = input("Ingrese su mes de cumpleaños: ")

#Clasificación
if mes == "1" and día >= 20 or mes == "2" and día <= 18:
    print("Eres Acuario.")
elif mes == "2" and día >= 19 or mes == "3" and día <= 20:
    print("Eres Piscis.")
elif mes == "3" and día >= 21 or mes == "4" and dia <= 20:
    print("Eres Aries.")
elif mes == "4" and día >= 21 or mes == "5" and día <= 21:
    print("Eres Tauro.")
elif mes == "5" and día >= 22 or mes == "6" and día <= 21:
    print("Eres Geminis.")
elif mes == "6" and día >= 22 or mes == "7" and día <= 23:
    print("Eres Cáncer.")
elif mes == "7" and día >= 24 or mes == "8" and día <= 23:
    print("Eres Leo.")
elif mes == "8" and día >= 24 or mes == "9" and día <= 23:
    print("Eres Virgo.")
elif mes == "9" and día >= 24 or mes == "10" and día <= 23:
    print("Eres Libra.")
elif mes == "10" and día >= 24 or mes == "11" and día <= 22:
    print("Eres Escorpión.")
elif mes == "11" and día >= 23 or mes == "12" and día <= 22:
    print("Eres Sagitario.")
else:
    print("Eres Capricornio.")
