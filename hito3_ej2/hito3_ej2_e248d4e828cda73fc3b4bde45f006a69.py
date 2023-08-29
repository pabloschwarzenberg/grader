class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []  # Inicializa el atributo subcategorias como una lista vacía

# Ejemplo de uso de la clase Taxon
ave = Taxon("Clase", "Aves")
print(ave.categoria)  # Imprime "Clase"
print(ave.nombre)  # Imprime "Aves"
print(ave.subcategorias)  # Imprime una lista vacía []
