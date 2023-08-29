class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre

# Ejemplo de uso
ave = Taxon("Clase", "Aves")
print(ave.categoria)  # Imprime: Clase
print(ave.nombre)  # Imprime: Aves