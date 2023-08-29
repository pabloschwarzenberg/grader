class Pokemon:
  def __init__(self,nombre,tipo,ataque):
    self.nombre=nombre
    self.level=random.randint(5,25)
    self.tipo=tipo
    self.ataque=ataque
    self.hp=self.level*3
  def __str__(self):
    string = ""
    string+= self.nombre
    string+="\n"+ str(self.level)
    string+="\n"+ (str(self.hp))
    string+="\n"+ (self.tipo)
    string+="\n"+ (self.ataque)  
    return string
class Entrenador:
  def __init__(self,nombre):
    self.nombre=nombre
    self.lista_pokemon=[]
  def agregar_poke(self):
    self.lista_pokemon.append()
  def __str__(self):
    return self.nombre

class Batalla:
  pass