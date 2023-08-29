# Definir una función que valide si una secuencia es válida o no
def validar_secuencia(secuencia):
  # Convertir la secuencia a mayúsculas
  secuencia = secuencia.upper()
  # Crear un conjunto con las letras válidas
  letras_validas = {"A", "C", "T", "G"}
  # Recorrer cada letra de la secuencia
  for letra in secuencia:
    # Si la letra no está en el conjunto de letras válidas, retornar False
    if letra not in letras_validas:
      return False
  # Si se recorrió toda la secuencia sin encontrar una letra inválida, retornar True
  return True

# Pedir al usuario que ingrese una secuencia
secuencia = input("Ingrese una secuencia: ")

# Llamar a la función validar_secuencia con la secuencia ingresada
resultado = validar_secuencia(secuencia)

# Imprimir el mensaje correspondiente según el resultado
if resultado:
  print("Secuencia correcta")
else:
  print("Secuencia incorrecta")