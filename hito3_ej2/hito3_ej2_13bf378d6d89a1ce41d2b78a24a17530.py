class Taxon:
    def init(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []


clase_aves = Taxon("Clase", "Aves")
orden_accipitriformes = Taxon("Orden", "Accipitriformes")
familia_accipitridae = Taxon("Familia", "Accipitridae")


clase_aves.subcategorias.append(orden_accipitriformes)
orden_accipitriformes.subcategorias.append(familia_accipitridae)


print(len(clase_aves.subcategorias)) 
print(orden_accipitriformes.nombre)
print(familia_accipitridae.categoria)