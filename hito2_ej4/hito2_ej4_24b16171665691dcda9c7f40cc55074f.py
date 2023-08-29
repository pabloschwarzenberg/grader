juegos = {1: 33.77, 2: 203, 3: 27.58, 4: 348, 5: 51.19}
lista_vacia = [] 
def agregar_juego(juegos, n_juegos):
    for x in range(n_juegos):
        lista_vacia.append(juegos)




def calcular_precio():
    final = sum([juegos[juego] for juego in lista_vacia])
    
    contador = 0
    if (1 in lista_vacia) and (2 in lista_vacia) and (3 in lista_vacia):
        contador = precio_total * 0.2
        
    elif (4 in lista_vacia) and (5 in lista_vacia):
        contador = final * 0.15
    final = final - contador
    
    return round(final, 1)

while True:
    y = input()
    if y == "checkout":
        print("El precio total es: USD", calcular_precio())
        break
        
    elif y == "ver":
        print("Los productos en el carro son:", carro)
        
    else:
        y = y.split(",")
        juego = int(y[0])
        n_juegos = int(y[1])
        agregar_juego(juego, n_juegos)
