# Pedir al usuario que ingrese un número de hasta 4 dígitos
numero = int(input("Ingrese un número de hasta 4 dígitos: "))

# Inicializar una variable para almacenar el resultado
resultado = ""

# Obtener las unidades del número usando el operador %
unidades = numero % 10
# Agregar las unidades al resultado con el símbolo U
resultado = str(unidades) + "U" + resultado

# Dividir el número por 10 y actualizarlo usando el operador //
numero = numero // 10

# Si el número aún tiene dígitos
if numero > 0:
  # Obtener las decenas del número usando el operador %
  decenas = numero % 10
  # Agregar las decenas al resultado con el símbolo D y un signo +
  resultado = str(decenas) + "D + " + resultado

  # Dividir el número por 10 y actualizarlo usando el operador //
  numero = numero // 10

  # Si el número aún tiene dígitos
  if numero > 0:
    # Obtener las centenas del número usando el operador %
    centenas = numero % 10
    # Agregar las centenas al resultado con el símbolo C y un signo +
    resultado = str(centenas) + "C + " + resultado

    # Dividir el número por 10 y actualizarlo usando el operador //
    numero = numero // 10

    # Si el número aún tiene dígitos
    if numero > 0:
      # Obtener los miles del número usando el operador %
      miles = numero % 10
      # Agregar los miles al resultado con el símbolo M y un signo +
      resultado = str(miles) + "M + " + resultado

# Imprimir el resultado
print(resultado)
