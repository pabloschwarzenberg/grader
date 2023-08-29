#Zodiaco
signo = ["Capricornio", "Acuario", "Piscis", "Aries", "Tauro", "Geminis", "Cancer", "Leo", "Virgo", "Libra", "Escorpio", "Sagitario"]
fecha = [20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21]
mes = int(input("Ingrese su mes de namiento: "))
dia = int(input("Ingrese su día de nacimiento: "))
mes = mes - 1
if dia > fecha(mes): 
    mes = mes + 1
if mes == 12: 
    mes = 0 
print("Tu signo es:", signo(mes))      