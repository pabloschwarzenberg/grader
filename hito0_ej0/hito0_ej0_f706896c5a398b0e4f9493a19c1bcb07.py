class Pokemon:
    def __init__(self,nombre,tipo):
        self.nombre=nombre
        self.tipo=tipo
        self.nivel=1
        self.vida=1

    def get_ataque(self):
        ataque=random.randint(0,(self.nivel/25)*2.6)
        return ataque
        
    def nivel(self):
        self.nivel=random.randint(5,25)

    def vida(self):
        self.vida=self.nivel*3

    def __repr__(self):
        return self.nombre
class Entrenador:

    def __init__ (self,nombre):
        self.nombre=nombre
        self.lista=[]

    def agregar(self,pokemon):
        if len(self.lista)<6:
            self.lista.append(pokemon)
            return True
        else:
            return False

    def mostar(self):
        for pokemons in self.lista:
            print("el nombre es: ",pokemons.nombre," vida: ",pokemons.vida," nivel: ",pokemons.nivel)
class Batalla:
        pass
()
      