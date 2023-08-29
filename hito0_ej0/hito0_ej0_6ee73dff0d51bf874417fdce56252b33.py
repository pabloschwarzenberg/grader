import random
class pokemon:
    def __init__(self,nombre,tipo,ataque,ataque_tipo):
        nivel=random.randint(5,26)
        self.nombre=nombre
        self.nivel=nivel
        self.tipo=tipo
        self.ataque=ataque+' '+ataque_tipo
        self.hp=nivel*3


lista_pokemon=[]
archivo_datos=open('pokemon.csv','r')
for linea in archivo_datos:
    linea=linea.strip()
    linea=linea.split(',')

    lista_pokemon.append(linea)
    
    print(linea)

print(lista_pokemon)

archivo_datos.close()

print("Qué pokemon deseas escojer")
contador=1
for i in lista_pokemon:
    contador=str(contador)
    print(contador + ")"+ i[0])
    contador=int(contador)
    contador+=1

