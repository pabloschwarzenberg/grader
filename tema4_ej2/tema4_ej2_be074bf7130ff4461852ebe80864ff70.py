class auto:
    def __init__(self):
        self.marca = ""
        self.modelo = ""
        self.color = ""
        self.kms = 0
    def __str__(self):
        return "Auto:\nMarca: "+self.marca+"\nModelo: "+self.modelo+"\nColor: "+self.color+"\nKilometraje: "+str(self.kms)
    

auto1 = auto()
print(auto1)