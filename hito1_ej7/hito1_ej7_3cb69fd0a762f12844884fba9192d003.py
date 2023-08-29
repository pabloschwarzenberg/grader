Signos = ["Capricornio","Acuario","Piscis","Aries","Tauro","Géminis","Cáncer","Leo","Virgo","Libra","Escorpio","Sagitario"]

Fechas = [19,18,20,19,21,20,23,21,24,23,21,21]

dia = int(input("Favor ingrese su dia de nacimiento:"))

mes = int(input("Favor ingrese su mes de nacimiento:"))

if mes == 12:
    
  mes = 0

if dia > Fechas[mes]:

  mes = mes+1


print(Signos[mes-1])      