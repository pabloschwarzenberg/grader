# Leer el string con la secuencia y convertirlo a mayúsculas
secuencia = input("Ingrese una secuencia: ").upper()

# Definir una variable con las letras válidas para un genoma
validas = "ACTG"

# Inicializar una variable booleana para indicar si la secuencia es válida o no
es_valida = True

# Recorrer cada letra de la secuencia y verificar si pertenece a las letras válidas
for letra in secuencia:
  if letra not in validas:
    # Si la letra no es válida, cambiar el valor de la variable booleana y salir del bucle
    es_valida = False
    break

# Usar un condicional if-else para imprimir el mensaje correspondiente
if es_valida:
  print("Secuencia correcta")
else:
  print("Secuencia incorrecta")
