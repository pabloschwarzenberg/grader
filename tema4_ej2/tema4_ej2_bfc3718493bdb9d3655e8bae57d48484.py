# Declaración de la clase
class Auto:
    def __init__(self,ma,mo,c,k):
        self.marca = ma
        self.modelo = mo
        self.color = c
        self.kms = k
    def __str__(self):
        return "Auto:\nMarca: "+self.marca+"\nModelo: "+self.modelo+"\nColor: "+self.color+"\nKilometraje: "+str(self.kms)

# Instanciación o creación del objeto
auto1 = Auto("Fiat","Uno","Rojo",0)
print(auto1,0)
