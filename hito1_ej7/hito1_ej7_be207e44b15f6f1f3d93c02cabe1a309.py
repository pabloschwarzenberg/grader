# Definir una función que recibe el día y el mes del cumpleaños
def signo_zodiaco(dia, mes):
  # Definir una lista con los nombres de los signos del zodíaco
  signos = ["Capricornio", "Acuario", "Piscis", "Aries", "Tauro", "Géminis", "Cáncer", "Leo", "Virgo", "Libra", "Escorpio", "Sagitario"]
  # Definir una lista con las fechas límite de cada signo
  limites = [20, 19, 20, 20, 21, 21, 22, 23, 23, 23, 22, 21]
  # Si el día es menor o igual al límite del mes correspondiente
  if dia <= limites[mes - 1]:
    # El signo es el mismo que el índice del mes
    signo = signos[mes - 1]
  else:
    # El signo es el siguiente al índice del mes
    signo = signos[mes % 12]
  # Imprimir el signo
  print("Tu signo del zodíaco es:", signo)

# Pedir al usuario que ingrese el día y el mes de su cumpleaños
dia = int(input("Ingresa el día de tu cumpleaños: "))
mes = int(input("Ingresa el mes de tu cumpleaños: "))
# Llamar a la función con los datos ingresados
signo_zodiaco(dia, mes)
