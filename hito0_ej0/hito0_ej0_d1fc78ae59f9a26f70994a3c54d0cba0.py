if __name__ == "__main__":
  from random import randint


  class Pokemon:
      def __init__(self, nombre, tipo):
          self.nombre = nombre
          self.tipo = tipo
          self.nivel = randint(5, 26)
          self.vida = self.nivel * 3

  class Entrenador:
      def __init__(self, name):
          self.nombre = name
          self.pokemones = []

      def agregar_pokemon(self, pokedex):
          print("Esta es la pokedex")
          for pk in pokedex:
              print(pokedex.index(pk), pk.nombre, "--- Tipo", pk.tipo)
          print("Elige tus 6 pokemones")
          for i in range(0, 6):
              try:
                  pokemon_index = int(input("Escribe el numero de la pokedex del pokemon que deseas: "))
                  self.pokemones.append([pokedex[pokemon_index], 0])
                  print("¡Agregado!")
              except IndexError:
                  print("Intentelo de nuevo")
              except ValueError:
                  print("Ese numero no existe")
          print("Tu lista de pokemones esta llena")

      def reordenar_pokemones(self):
          print("Tu lista de pokemones es: ")
          for pokemon in self.pokemones:
              print(pokemon[0].nombre)
          print("¿Que pokemon deseas cambiar de posicion?")
          p = int(input("Escribe su lugar en tu lista (empieza en la posicion cero) : "))
          n = int(input("Escribe donde quieres que este (empieza en la posicion cero) : "))
          self.pokemones.insert(p, self.pokemones[n])
          a = self.pokemones[n + 1]
          self.pokemones.pop(n + 1)
          self.pokemones.insert(p, a)
          self.pokemones.pop(p + 1)

      def mostrar_pokemones(self):
          for pok in self.pokemones:
              print(str(pok[0].nombre) + ": Nivel " + str(pok[0].nivel) + ", Vida " + str(pok[0].vida) + ", Tipo " + str(
                  pok[0].tipo) + ".")
          print("Pokemon de batalla: " + self.pokemones[0][0].nombre)


  class Batalla:
      def __init__(self, luchador1, luchador2):
          self.contrincantes = []
          if isinstance(luchador1, Entrenador) and isinstance(luchador2, Entrenador):
              if luchador1.pokemones[0][0].nivel > luchador2.pokemones[0][0].nivel:
                  self.contrincantes.append(luchador1)
                  self.contrincantes.append(luchador2)
              else:
                  self.contrincantes.append(luchador2)
                  self.contrincantes.append(luchador1)

      def recuperar_pokemon(self, contrincante):
          # Contrincante es 1 o 2, y luego el entrenador 1 o 2
          contrincante = self.contrincantes[self.contrincantes.index(contrincante)]
          for i in range(0, 6):
              pokemon_elegido = input("Ingrese nombre de Pokemon:")
              # Nombre del pokemon
              for k in contrincante.pokemones:
                  if k == [pokemon_elegido, 0]:
                      print("Gastas una pocion. Te queda una.")
                      pokemon_elegido = k[0]
                      # Objeto pokemon
                      pokemon_elegido.vida += 20
                  if k == [pokemon_elegido, 1]:
                      print("Gastas una pocion. Te has quedado sin pociones.")
                      pokemon_elegido = k[0]
                      #  Objeto pokemon
                      pokemon_elegido.vida += 20
                  else:
                      print("No puedes curar más a este pokemon")
                      return False
                      # False nos permitira volver a preguntar

      def reordenar_pokemones(self, jugador):
          jugador = self.contrincantes[self.contrincantes.index(jugador)]
          print("Tu lista de pokemones es: ")
          for pokemon in jugador.pokemones:
              print(pokemon[0])
          print("¿Que pokemon deseas cambiar de posicion?")
          p = int(input("Escribe su lugar en tu lista (empieza en la posicion cero) : "))
          n = int(input("Escribe donde quieres que este (empieza en la posicion cero) : "))
          jugador.pokemones.insert(p, jugador.pokemones[n])
          a = jugador.pokemones[n + 1]
          jugador.pokemones.pop(n + 1)
          jugador.pokemones.insert(p, a)
          jugador.pokemones.pop(p + 1)

      def atacar(self, atacante):
          if self.contrincantes.index(atacante) != -1:
              if self.contrincantes.index(atacante) == 1:
                  objetivo = self.contrincantes[0]
              else:
                  objetivo = self.contrincantes[1]
              pk_atacante = atacante.pokemones[0][0]
              pk_objetivo = objetivo.pokemones[0][0]
              daño = randint(0, int(((pk_atacante.nivel) / 25) * 2.6))
              if pk_atacante.tipo == "agua" and pk_objetivo.tipo == "fuego":
                  daño = 2 * daño
              if pk_atacante.tipo == "agua" and pk_objetivo.tipo == "hierba":
                  daño = 0.5 * daño
              if pk_atacante.tipo == "agua" and pk_objetivo.tipo == "agua":
                  daño = 0.5 * daño
              if pk_atacante.tipo == "fuego" and pk_objetivo.tipo == "fuego":
                  daño = 0.5 * daño
              if pk_atacante.tipo == "fuego" and pk_objetivo.tipo == "hierba":
                  daño = 2 * daño
              if pk_atacante.tipo == "fuego" and pk_objetivo.tipo == "agua":
                  daño = 0.5 * daño
              if pk_atacante.tipo == "electricidad" and pk_objetivo.tipo == "hierba":
                  daño = 0.5 * daño
              if pk_atacante.tipo == "electricidad" and pk_objetivo.tipo == "agua":
                daño = 2 * daño
              if pk_atacante.tipo == "electricidad" and pk_objetivo.tipo == "electricidad":
                  daño = 0.5 * daño
              if pk_atacante.tipo == "hierba" and pk_objetivo.tipo == "fuego":
                  daño = 0.5 * daño
              if pk_atacante.tipo == "hierba" and pk_objetivo.tipo == "hierba":
                  daño = 0.5 * daño
              if pk_atacante.tipo == "hierba" and pk_objetivo.tipo == "agua":
                  daño = 2 * daño
              return daño

      def ganador(self):
          if self.contrincantes[0].pokemones[0][0].vida == 0 and self.contrincantes[0].pokemones[0][1].vida == 0 and \
                          self.contrincantes[0].pokemones[0][2].vida == 0 and self.contrincantes[0].pokemones[0][
              3].vida == 0 and self.contrincantes[0].pokemones[0][4].vida == 0 and self.contrincantes[0].pokemones[0][
              5].vida == 0:
              print(self.contrincantes[1].nombre, "ha ganado.")
              return True
          elif self.contrincantes[1].pokemones[0][0].vida == 0 and self.contrincantes[1].pokemones[0][1].vida == 0 and \
                          self.contrincantes[1].pokemones[0][2].vida == 0 and self.contrincantes[1].pokemones[0][
              3].vida == 0 and self.contrincantes[1].pokemones[0][4].vida == 0 and self.contrincantes[1].pokemones[0][
              5].vida == 0:
              print(self.contrincantes[0].nombre, "ha ganado.")
              return True
          else:
              return False


# Flujo

  print("Bienvenidos a la arena pokemon")

  print("Detectando cartucho")
# Utilización de Archivo para creación de lista con pokemones
# Debe tomar el nombre y el tipo para crear un objeto pk
  pokemons = open("Pokemons.txt", "r")
  pokedex = []
  for linea in pokemons:
      linea = linea.strip()
      linea = linea.split(",")
      linea = Pokemon(linea[0], linea[1])
      pokedex.append(linea)
  pokemons.close()
  print("Pokedex detectada")

  luchador1 = input("Bienvenido, primer entrenador, ¿Cual es tu nombre? ")
  luchador1 = Entrenador(luchador1)
  luchador1.agregar_pokemon(pokedex)
  luchador1.mostrar_pokemones()
  while True:
      reordenar = input("¿Desea reordenar sus pokemones? Si: S  ")
      if reordenar.upper() == "S":
          luchador1.reordenar_pokemones()
          print("")
          luchador1.mostrar_pokemones()
      else:
          break

  luchador2 = input("Bienvenido, segundo entrenador, ¿Cual es tu nombre? ")
  luchador2 = Entrenador(luchador2)
  luchador2.agregar_pokemon(pokedex)
  luchador2.mostrar_pokemones()
  while True:
      reordenar = input("¿Desea reordenar sus pokemones? Si: S  ")
      if reordenar.upper() == "S":
          luchador2.reordenar_pokemones()
          print("")
          luchador2.mostrar_pokemones()
      else:
          break

  print("¡Todo listo!")
  batalla = Batalla(luchador1, luchador2)
  while batalla.ganador() == False:
      print("Turno de",batalla.contrincantes[0].nombre)
      while True:
          decision = input("Escriba A para ATACAR, R para RECUPERAR y C para CAMBIAR  ")
          if decision.upper() == "A":
              print(batalla.contrincantes[0].pokemones[0][0].nombre, "ATACA")
              print("Daño:",batalla.atacar(batalla.contrincantes[0]))
              batalla.contrincantes[1].pokemones[0][0].vida -= batalla.atacar(batalla.contrincantes[0])
  
              if batalla.contrincantes[1].pokemones[0][0].vida <= 0:
                  batalla.contrincantes[1].pokemones.insert(0, batalla.contrincantes[1].pokemones[1])
                  batalla.contrincantes[1].pokemones.append(batalla.contrincantes[1].pokemones[0])
                  batalla.contrincantes[1].pokemones.pop(1)
              break
          elif decision.upper() == "R":
              batalla.recuperar_pokemon(batalla.contrincantes[0])
              break
          elif decision.upper() == "C":
              batalla.reordenar_pokemones(batalla.contrincantes[0])
              break
          else:
              print("Intentelo de nuevo")
 