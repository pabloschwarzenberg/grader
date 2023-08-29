#Zodiaco
día = int(input("Ingrese el día de su nacimiento(número): "))
mes = int(input("Ingrese el mes de su nacimiento(número): "))
mes = mes - 1

#Sistema de listas ordenado
z = ["Capricornio", "Acuario","Piscis","Aries","Tauro","Geminis","Cancer","Leo","Virgo","Libra","Escorpio","Sargitario"]
l = [20,19,20,20,21,21,22,22,22,22,22,21]
x = [23,21,22,22,21,22,24,24,24,24,24,25]

#Condicionantes del zodiaco [+ 20 puntos de estilo]
if mes == 12:
    mes = 0
    
if día > l[mes]:
    mes = mes + 1

if día < x[mes]:
    x = l

print(z[mes])  