import random as p
#archivo_datos = open("pokemon.csv","r")
lista_nombres=[]
lista_tipos=[]
#for Linea in archivo_datos :
    Linea = Linea.strip()
    Linea = Linea.split(",")
    lista_nombres.append(Linea[0])
    lista_tipos.append(Linea[1])

archivo_datos.close()
class Pokemon :
    ataques=[["Impactrueno","Electrico"],["Chispa","Electrico"],["Voltio Cruel","Electrico"],["Onda Voltio","Electrico"],["Colmillo Ígneo","Fuego"],["Ascuas","Fuego"],
             ["Llamarada","Fuego"],["Rueda Fuego","Fuego"],["Latigosepa","Hierva"],["Hoja Afilada","Hierva"],
             ["Rayo Solar","Hierva"],["Bullet Seed","Hierva"],["Rayo Burbuja","Agua"],["Surf","Agua"],["Hidrocañón","Agua"],["Surf","Agua"]]
    def __init__(self,nombre,tipo,HP,ataques,nivel,recuperadas):
        self.tipo = tipo
        self.nombre = nombre
        self.HP = HP
        self.ataques = ataques
        self.nivel = nivel
        self.recuperadas=recuperadas

    def generar_pokemon(self):
        recuperadas = 0
        todos_pokemons = []
        pokemon_local = []
        ataques = [["Impactrueno", "Electrico"], ["Chispa", "Electrico"], ["Voltio Cruel", "Electrico"],
                   ["Onda Voltio", "Electrico"], ["Colmillo Ígneo", "Fuego"], ["Ascuas", "Fuego"],
                   ["Llamarada", "Fuego"], ["Rueda Fuego", "Fuego"], ["Latigosepa", "Hierva"],
                   ["Hoja Afilada", "Hierva"],
                   ["Rayo Solar", "Hierva"], ["Bullet Seed", "Hierva"], ["Rayo Burbuja", "Agua"], ["Surf", "Agua"],
                   ["Hidrocañón", "Agua"], ["Surf", "Agua"]]
        for i in range(len(lista_nombres)):
            pokemon_local.append(lista_nombres[i])
            pokemon_local.append(lista_tipos[i])
            nivel = p.randint(5,25)
            pokemon_local.append(nivel)
            HP = 3*(nivel)
            pokemon_local.append(HP)
            pokemon_local.append(recuperadas)
            pokemon_local.append(ataques[i])
            todos_pokemons.append(pokemon_local)
            pokemon_local=[]

        return todos_pokemons
        pass
class Entrenador:
        pass
class Batalla:
        pass
      