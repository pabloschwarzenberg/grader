class Taxon:
	pass
    aves = Taxon("Clase", "Aves")
falconiformes = Taxon("Orden", "Falconiformes")
passeriformes = Taxon("Orden", "Passeriformes")

aves.subcategorias.append(falconiformes)
aves.subcategorias.append(passeriformes)
  