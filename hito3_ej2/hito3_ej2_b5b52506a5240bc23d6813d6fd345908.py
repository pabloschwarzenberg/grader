class Taxon:
    def __init__(self, category, name):
        self.category = category
        self.name = name

    sc = []
    def sc(self, scategory):
        self.sc = scategory


ave = Taxon("paloma", "hola")