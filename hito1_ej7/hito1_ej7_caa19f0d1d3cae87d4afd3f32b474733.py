#Zodiaco
def Signo_del_Zodiaco(dia, mes):
  if (mes == 1 and 20 <= dia <= 31) or (mes == 2 and 1 <= dia <= 18):
    return "Acuario"
  elif (mes == 2 and 19 <= dia <= 29) or (mes == 3 and 1 <= dia <= 20):
    return "Piscis"
  elif (mes == 3 and 21 <= dia <= 31) or (mes == 4 and 1 <= dia <= 19):
    return "Aries"
  elif (mes == 4 and 20 <= dia <= 30) or (mes == 5 and 1 <= dia <= 20):
    return "Tauro"
  elif (mes == 5 and 21 <= dia <= 31) or (mes == 6 and 1 <= dia <= 20):
    return "Geminis"
  elif (mes == 6 and 21 <= dia <= 30) or (mes  == 7 and 1 <= dia <= 22):
    return "Cancer"
  elif (mes == 7 and 23 <= dia <= 31) or (mes == 8 and 1<=  dia <= 22):
    return "Leo"
  elif (mes == 8 and 23 <= dia <= 30) or (mes == 9 and 1 <= dia <= 22):
    return  "Virgo"
  elif (mes == 9 and 23 <= dia <= 30) or (mes == 10 and 1 <= dia <= 22):
    return "Libra"
  elif (mes == 10 and  23 <= dia <= 31) or (mes == 11 and 1 <= dia <= 21):
    return "Escorpio"
  elif (mes == 11 and 22 <= dia <= 30) or (mes == 12 and 1 <= dia <= 21):
    return "Sagitario"
  elif (mes == 12 and 22 <= dia <= 31)  or (mes == 1 and 1 <= dia <= 19):
    return "Capricornio"
  else:
    return "Fecha de cumpleanos invalida"
    
Dia_de_cumpleanos = int(input("Ingrese el dia de su compleanos(1-31):"))
Mes_de_cumpleanos = int(input("Ingrese el mes de cumpleanis (1-12):"))
Signo_zodiaco = Signo_del_Zodiaco(Dia_de_cumpleanos, Mes_de_cumpleanos)
print("El signo del zodiaco es:", Signo_zodiaco)