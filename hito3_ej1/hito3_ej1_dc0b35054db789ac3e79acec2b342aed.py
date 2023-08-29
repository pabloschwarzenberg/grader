class Taxon:
  # Inicializar los atributos de la clase
  def __init__(self, categoria, nombre):
    self.categoria = categoria
    self.nombre = nombre

  # Definir un método para mostrar la información del taxon
  def mostrar(self):
    print("El taxon es de categoría", self.categoria, "y se llama ", self.nombre)

# Crear un objeto de la clase Taxon
aves = Taxon("Clase", "Aves")

# Mostrar la información del objeto
aves.mostrar()
      