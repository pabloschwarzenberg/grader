#Contestador de celular
      
numero = input("Ingrese número telefónico: ")
valor_hora = input("Ingrese hora de la llamada: ")

# El número telefónico debe ser representado por un número entero (int) de 8 cifras
if (len(numero) == 8):

  #la hora es representada por un número entero entre 0 y 23
  if valor_hora.isdigit() and (int(valor_hora) >= 0 and int(valor_hora) <= 23):

    hora = int(valor_hora)

    #Es emergencia
    if  ((hora >= 0 and hora <= 7) or
         (hora < 14 and numero[5:8:1] == '909') or
         (hora >= 17 and hora <= 19 and numero[0:3:1] != '877')):
         print("Resultado: CONTESTAR")
    else:
      print("Resultado: NO CONTESTAR")
  else:
    print("Debe indicar una hora válida")
else:
  print("El número de teléfono debe tener 8 caracteres numéricos")