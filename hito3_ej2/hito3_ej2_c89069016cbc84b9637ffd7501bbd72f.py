class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

# Ejemplo de uso
taxon_clase_aves = Taxon("Clase", "Aves")
taxon_orden_accipitriformes = Taxon("Orden", "Accipitriformes")

taxon_clase_aves.subcategorias.append(taxon_orden_accipitriformes)

print(taxon_clase_aves.subcategorias)  # Output: [<__main__.Taxon object at 0x...>]
