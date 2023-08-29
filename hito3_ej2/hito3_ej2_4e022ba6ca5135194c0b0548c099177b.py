# Crear una instancia de Taxon
clase_aves = Taxon("Clase", "Aves")

# Crear subcategorías
orden = Taxon("Orden", "Passeriformes")
familia = Taxon("Familia", "Turdidae")

# Agregar subcategorías al taxón
clase_aves.subcategorias.append(orden)
clase_aves.subcategorias.append(familia)
