# Definimos una función que valida si una cadena es una secuencia de genoma válida
def validar_secuencia_genoma(cadena):
  # Convertimos la cadena a mayúsculas para no distinguir entre mayúsculas y minúsculas
  cadena = cadena.upper()
  # Definimos las letras válidas para una secuencia de genoma
  letras_validas = "ACTG"
  # Recorremos cada letra de la cadena y verificamos si está en las letras válidas
  for letra in cadena:
    if letra not in letras_validas:
      # Si encontramos una letra inválida, retornamos False
      return False
  # Si todas las letras son válidas, retornamos True
  return True

# Pedimos al usuario que ingrese una cadena
cadena = input("Ingrese una cadena: ")
# Validamos si la cadena es una secuencia de genoma válida
es_valida = validar_secuencia_genoma(cadena)
# Imprimimos el resultado según el valor de es_valida
if es_valida:
  print("Secuencia correcta")
else:
  print("Secuencia incorrecta")
