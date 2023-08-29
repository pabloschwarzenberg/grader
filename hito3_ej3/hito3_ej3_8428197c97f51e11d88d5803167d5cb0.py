class Taxon:
    def _init_(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)

# Creamos el Taxon Clase Aves
aves = Taxon("Clase", "Aves")

# Creamos el Taxon Orden Falconiformes
falconiformes = Taxon("Orden", "Falconiformes")

# Agregamos el Taxon Orden Falconiformes como subcategoría del Taxon Clase Aves
aves.incluir(falconiformes)

# Agregamos más subcategorías al Taxon Orden Falconiformes
halcones = Taxon("Familia", "Halcones")
aguilas = Taxon("Familia", "Águilas")
falconiformes.incluir(halcones)
falconiformes.incluir(aguilas)

# Imprimimos la información del Taxon Clase Aves
print(f"{aves.categoria} {aves.nombre}")
for subcat1 in aves.subcategorias:
    print(f"  {subcat1.categoria} {subcat1.nombre}")
    for subcat2 in subcat1.subcategorias:
        print(f"    {subcat2.categoria} {subcat2.nombre}")