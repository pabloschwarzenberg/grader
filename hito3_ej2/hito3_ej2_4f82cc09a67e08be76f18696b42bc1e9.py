ave = Taxon("Clase", "Aves")
orden = Taxon("Orden", "Falconiformes")
familia = Taxon("Familia", "Falconidae")

# Agregar subcategorías al taxón "ave"
ave.subcategorias.append(orden)
orden.subcategorias.append(familia)

# Acceder a las subcategorías del taxón "ave"
print(ave.subcategorias)  # Imprime: [<__main__.Taxon object at 0x...>]
print(ave.subcategorias[0].nombre)  # Imprime: Falconiformes
print(ave.subcategorias[0].subcategorias[0].nombre)  # Imprime: Falconidae
