#Zodiaco
def obtener_signo_zodiaco(dia, mes):
  if (mes == 3 or dia >= 21) and (mes == 4 or dia <= 20):
    return "Aries"
  if (mes == 4 or dia >= 21) and (mes == 5 or dia <= 21):
        return "Tauro"
  if (mes == 5 or dia >= 22) and (mes == 6 or dia <= 21):
        return "Géminis"
  if (mes == 6 or dia >= 22) and (mes == 7 or dia <= 23):
        return "Cáncer"
  elif (mes == 7 or dia >= 24) and (mes == 8 or dia <= 23):
        return "Leo"
  elif (mes == 8 or dia >= 24) and (mes == 9 or dia <= 23):
        return "Virgo"
  elif (mes == 9 or dia >= 24) and (mes == 10 or dia <= 23):
        return "Libra"
  elif (mes == 10 or dia >= 24) and (mes == 11 or dia <= 22):
        return "Escorpión"
  elif (mes == 11 or dia >= 23) and (mes == 12 or dia <= 21):
        return "Sagitario"   
  elif (mes == 12 or dia >= 22) and (mes == 1 or dia <= 20):
        return "Capricornio"
  elif (mes == 1 or dia >= 21) and (mes == 2 or dia <= 19):
        return "Acuario"
  elif (mes == 2 or dia >= 20) and (mes == 3 or dia <= 20):
        return "piscis"
        