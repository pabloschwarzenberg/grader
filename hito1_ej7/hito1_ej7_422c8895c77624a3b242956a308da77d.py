#Zodiaco
def obtener_signo(dia, mes):
  if (mes == 1 and dia >= 20) or(mes == 2 and dia <= 18):
    return "Acuario"
  elif(mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
    return "Piscis"
  elif(mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
    return "Aries"
  elif(mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
    return "Tauro"
  elif(mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
    return "Geminis"
  elif(mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
    return "Cancer"
  elif(mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
    return "Leo"
  elif(mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
    return "Virgo"
  elif(mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
    return "Libra"
  elif(mes == 10 and dia >= 23) or (mes == 11 and dia <= 22):
    return "Escorpio"
    return
  elif(mes == 11 and dia >= 23) or (mes == 12 and dia <= 22):
    return "Sagitario"
  else:
    return "Capricornio"

dia = int(input("ingrese el dia de su cumpleaños(1-31): "))
mes = int(input("ingrese el mes de su cumpleaños(1-12): "))
signo = obtener_signo(dia, mes)
print("su signo del zodiaco es:", signo)