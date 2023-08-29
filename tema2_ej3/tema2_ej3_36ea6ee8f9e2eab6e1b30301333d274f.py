def numero_perfecto(x):
#ENTRADA Y PROCESAMIENTO:
    number = 0
    for i in range(1, x):
          if x%i == 0:
#NUMERO PERFECTO:
              number +=i
#SALIDA DEL NUMERO PERFECTO:
    return number == x
    