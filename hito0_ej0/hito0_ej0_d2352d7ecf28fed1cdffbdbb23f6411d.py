import random
class Pokemon:
  def _init_(self,nombre,tipo):
    self.nombre = nombre
    self.nivel = random.randint(5,25)
    self.tipo = tipo
    self.ataque = [self.nombre, self.tipo]
    self.HP = self.nivel * 3
    
class Entrenador:
  def _init_(self,):
    self.nombre = nombre
    self.pokemones = ["","","","","",""]

  def _str_(self):
    #Mostrar pokemones, nivel y HP
    pass

  def crear_entrenador(self):
    pass

  def elegir_pokemones(self):
    pass
    
class Batalla:
  def _init_(self,entrenador1,enternador2):
    self.contrincantes = [entrenador1,entrenador2]

  def atacar(self):
    #Ataca el de mayor nivel
    pass
    

  def CambiarPokemon(self):
    #primero el cambio, luego ataca
    pass

  def recuperar(self):
    #recuperar
    pass
    
pokemones=[]
#archivo_datos = open("pokemon.csv","r")
#for linea in archivo_datos:
 #   linea = linea.strip()
  #  linea = linea.split(",")
   # pokemon= Pokemon(linea[0],linea[1])
    #pokemones.append(pokemon)
#archivo_datos.close()

#for pokemon in pokemones:
 #   print(pokemon.nombre)
      