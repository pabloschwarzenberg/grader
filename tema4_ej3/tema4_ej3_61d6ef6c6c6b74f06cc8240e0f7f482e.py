# Declaración de la función
def jerigonzo(string):
    n_string = ""
    for c in string:
        if c=="a" or c=="e" or c=="i" or c=="o" or c=="u":
            n_string = n_string + c + "p" + c
        else:
            n_string += c
    return n_string
# Programa principal
if __name__ == "__main__":
  print("Jerigonzo")
  op = "S"
  while op=="S":
      # Captura de datos
      s = input("Ingrese su mensaje: ")
      # Procesamiento
      m_j = jerigonzo(s) # Invocación de la función
      # Exposición de resultados
      print("Su mensaje en Jerigonzo:",m_j)
      op = input("Ejecutar otra vez? S/N: ")
      op = op.upper()
