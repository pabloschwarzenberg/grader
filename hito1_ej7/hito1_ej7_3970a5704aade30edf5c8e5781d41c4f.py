#Zodiaco
signos_zodiacales = ["Capricornio" , "Acuario", "Piscis", "Aries" , "Tauro" , "Geminis" , "Cancer" , "Leo" , "Virgo" , "Libra" , "Escorpio" , "Sagitario"]
fecha = [20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21]
dia = int(input("inserte el dia de su nacimiento: "))
mes = int(input("inserte su mes de nacimiento: "))
mes = mes - 1
if dia > fecha[mes]:
    mes = mes + 1
if mes == 12:
    mes = 0
print(signos_zodiacales[mes])