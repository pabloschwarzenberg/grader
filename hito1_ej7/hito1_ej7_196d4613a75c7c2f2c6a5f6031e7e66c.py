#Zodiaco
Signos = ["Capricornio", "Acuario","Piscis", "Aries", "Tauro", "Geminis", "Cancer", "Leo", "Virgo", "Libra", "Escorpio", "Sagitario"]
Fechas = [19, 18, 20, 19, 20, 20, 22, 22, 22, 22, 21, 21]
dia = int(input("Ingrese su día de cumpleaños: "))
mes = int(input("Ingrese su mes de cumpleaños: "))

if dia > Fechas[mes]:
  mes = mes +1 
if mes == 12:
  mes = 0
  
print(Signos[mes-1])