class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

# Crear las instancias de Taxon después de definir la clase
aves = Taxon("Clase", "Aves")
orden = Taxon("Orden", "Passeriformes")
familia = Taxon("Familia", "Turdidae")

# Agregar las subcategorías
aves.subcategorias.append(orden)
orden.subcategorias.append(familia)
      