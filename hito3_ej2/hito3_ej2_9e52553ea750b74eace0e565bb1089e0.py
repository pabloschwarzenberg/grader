class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

# Ejemplo de uso
ave = Taxon("Clase", "Aves")
mamifero = Taxon("Clase", "Mamíferos")

ave.subcategorias.append(mamifero)

print(ave.categoria)  # Salida: Clase
print(ave.nombre)  # Salida: Aves
print(ave.subcategorias)  # Salida: [<__main__.Taxon object at 0x...>]

      