#Zodiaco
print("Ingrese su cumpleaños , el día y el mes :")
dia = int(input("Ingrese dia del 1 al 31: "))
mes = int(input("Ingrese mes del 1 al 12: "))
signo = ["Capricornio", "Acuario", "Piscis", "Aries", "Tauro", "Geminis", "Cancer", "Leo" , "Virgo", "Libra", "Escorpio", "Sagitario"]
fecha = [20 ,19 ,20 ,21 ,21 ,22 ,22 ,22 , 22, 22, 21]
mes = mes - 1
if dia > fecha[mes]:
    mes = mes + 1
else:
    if mes == 12:
        mes = 0
print("El signo zoodiacal es ", signo[mes])      