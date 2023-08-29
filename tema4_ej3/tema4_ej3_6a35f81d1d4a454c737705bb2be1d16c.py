def jerigonzo(texto):
  # Esta función recibe un texto y lo traduce a jerigonzo, agregando una p y repitiendo la vocal después de cada vocal
  # Creamos una lista vacía para guardar el texto traducido
  nuevo_texto = []
  # Recorremos el texto original por letra
  for letra in texto:
    # Agregamos la letra al nuevo texto
    nuevo_texto.append(letra)
    # Si la letra es una vocal
    if letra.lower() in "aeiou":
      nuevo_texto.append("p")
      nuevo_texto.append(letra)
  # Retornamos el nuevo texto como una cadena, uniendo los elementos de la lista con "".join()
  return "".join(nuevo_texto)

# Probamos la función con algunos ejemplos
if __name__ == "__main__":
  print(traducir_jerigonzo("Hola")) # Debe retornar "Hopolapa"
  print(traducir_jerigonzo("Python")) # Debe retornar "Pypothopon"
  print(traducir_jerigonzo("Jerigonzo")) # Debe retornar "Jeperipigoponzopo"
