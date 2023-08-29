#Zodiaco
Signos = ["Capricornio","Acuario","Piscis","Aries","Tauro","Géminis","Cáncer","Leo","Virgo","Libra","Escorpio","Sagitario"]
Fechas = [19,18,20,19,20,20,22,22,22,22,21,21]
dia = int(input("Digite su día de cumpleaños como número:"))
mes = int(input("Digite su mes de nacimiento como número:"))

if dia > Fechas[mes]:
    mes = mes+1
if mes == 12:
    mes = 0

print(Signos[mes-1])

          
     