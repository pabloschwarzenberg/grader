# Importar el módulo math para usar la función sqrt
import math

# Definir la clase vector
class Vector:
  # Definir el constructor de la clase
  def __init__(self, x, y, z):
    # Inicializar los atributos de la clase
    self.x = x
    self.y = y
    self.z = z

  # Definir el método norma de la clase
  def norma(self):
    # Calcular la norma del vector usando el teorema de Pitágoras
    return math.sqrt(self.x**2 + self.y**2 + self.z**2)

  # Definir el método __add__ de la clase para sobrecargar la operación +
  def __add__(self, other):
    # Sumar las componentes de los vectores y retornar un nuevo vector con el resultado
    return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

# Definir la función suma_vectores que recibe dos objetos de la clase Vector
def suma_vectores(v1, v2):
  # Usar el método __add__ de la clase Vector para sumar los vectores y retornar el resultado
  return v1 + v2
