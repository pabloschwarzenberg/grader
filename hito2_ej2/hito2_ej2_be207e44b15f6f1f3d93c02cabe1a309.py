# Definir una función que recibe un string y valida si es una secuencia del genoma
def validar_genoma(secuencia):
  # Definir una cadena con las letras válidas para el genoma
  letras = "ACTG"
  # Convertir el string a mayúsculas
  secuencia = secuencia.upper()
  # Recorrer cada caracter del string
  for caracter in secuencia:
    # Si el caracter no está en las letras válidas
    if caracter not in letras:
      # Retornar False
      return False
  # Si se recorrió todo el string sin encontrar caracteres inválidos, retornar True
  return True

# Pedir al usuario que ingrese un string
secuencia = input("Ingresa una secuencia: ")
# Llamar a la función con el string ingresado y guardar el resultado
resultado = validar_genoma(secuencia)
# Si el resultado es True, imprimir "secuencia correcta"
if resultado:
  print("secuencia correcta")
# Si el resultado es False, imprimir "secuencia incorrecta"
else:
  print("secuencia incorrecta")
