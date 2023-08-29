class Pokemon:
    def __init__(self, especie, nivel, tipo, ataque, HP):
        self.especie = especie
        self.nivel = nivel
        self.tipo = tipo
        self.ataque = ataque
        self.HP = HP

    def __str__(self):
        return "{}".format(self.especie)

    def ataque(self, ataque, tipo):
        self.ataque = ataque
        self.tipo = tipo
        return ataque, tipo

class Entrenador:
    def __init__(self, nombre, lista_pokemon):
        self.nombre = nombre
        self.lista_pokemon = lista_pokemon

    def __str__(self):
        return "{}".format(self.nombre)

    def mostrar_pokemon(self):      # Esta función es sólo para printear el equipo
        for pokemon in range(len(self.lista_pokemon)):
            print(self.lista_pokemon[pokemon])
        return "¡Este es tu equipo Pokémon!"

    def trabajar_pokemon(self, lista_pokemon):     # Con esta trabajaremos los pokemon
        return
class Batalla:
        pass
      