class pokemon:

    def init(self, nombre, tipo, color, danio):
        self.nombre = nombre
        self.tipo = tipo
        self.color = color
        self.danio = danio

    def atacar(self):
        return 3

    def habilidad(self):
        if(self.tipo == "agua"):
            print("3 de daño de agua")
        if(self.tipo == "fuego"):
            print("3 de daño de fuego")



charmander = pokemon("Charmander", "fuego", "rojo", 3)
magikarp = pokemon("Alberto","agua","azul", 0)
moltres = pokemon("Moltrez", "fuego", "arojoso", 150)


if(charmander.danio + charmander.atacar() >= magikarp.danio + magikarp.atacar()):
    print(f"{charmander.nombre} hace mas daño que {magikarp.nombre}")
else:
    print(f"{magikarp.nombre} hace mas daño que {charmander.nombre}")

magikarp.danio = 4


if(charmander.danio + charmander.atacar() >= magikarp.danio + magikarp.atacar()):
    print(f"{charmander.nombre} hace mas daño que {magikarp.nombre}")
else:
    print(f"{magikarp.nombre} hace mas daño que {charmander.nombre}")
      