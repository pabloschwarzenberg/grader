# Importar el módulo math para usar la función sqrt
import math

# Definir la clase Ciudad
class Ciudad:
  # Definir el constructor de la clase
  def __init__(self, x, y):
    # Inicializar los atributos de la clase
    self.x = x
    self.y = y

  # Definir el método camino de la clase
  def camino(self, other):
    # Crear una lista vacía para guardar los pasos
    pasos = []
    # Crear dos variables para guardar las coordenadas actuales
    x_actual = self.x
    y_actual = self.y
    # Agregar el punto inicial a la lista de pasos
    pasos.append([x_actual, y_actual])
    # Mientras no se llegue al punto final, repetir el siguiente proceso
    while x_actual != other.x or y_actual != other.y:
      # Si la coordenada x actual es menor que la del punto final, aumentarla en uno
      if x_actual < other.x:
        x_actual += 1
      # Si la coordenada x actual es mayor que la del punto final, disminuirla en uno
      elif x_actual > other.x:
        x_actual -= 1
      # Si la coordenada y actual es menor que la del punto final, aumentarla en uno
      if y_actual < other.y:
        y_actual += 1
      # Si la coordenada y actual es mayor que la del punto final, disminuirla en uno
      elif y_actual > other.y:
        y_actual -= 1
      # Agregar el punto actual a la lista de pasos
      pasos.append([x_actual, y_actual])
    # Retornar la lista de pasos como el resultado del método
    return pasos

  # Definir el método distancia de la clase
  def distancia(self, other):
    # Calcular la distancia entre los puntos usando el teorema de Pitágoras
    return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)

if __name__ == "__main__":
  # Crear dos objetos de la clase Ciudad con las coordenadas dadas
  p1 = Ciudad(1, 1)
  p2 = Ciudad(3, 3)
  # Llamar al método camino para generar los pasos entre las ciudades e imprimirlos
  print("Los pasos son:", p1.camino(p2))
  # Llamar al método distancia para calcular la distancia entre las ciudades e imprimirlo
  print("La distancia es:", p1.distancia(p2))

         