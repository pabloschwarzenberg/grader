class Taxon:
    def _init_(self, nombre):
        self.nombre = nombre
        self.subcategorias = []
    def incluir(self, subcategoria):
        self.subcategorias.append(subcategoria)
# Función para crear la jerarquía de taxones
def crear_jerarquia(taxon_principal, taxon_secundario):
    taxon_principal.incluir(taxon_secundario)
# Ejemplo de uso:
def __init__(self, Taxon):
        self.Taxon = Taxon