def jugar():
    global letrasEscritas
    global intentos
    intentos = 7
    letrasEscritas = []
    palabra = obtenerPalabra()
    prepararPalabra(palabra)
    while True:
        imprimirAhorcado()
        dibujarIntentos()
    print palabra()
        descubrirLetra(input("Ingresa la letra: "))
        if intentos <= 0:
            print("Perdiste. La palabra era: ")
            print PalabraOriginal()
            return
        if haGanado():
            print("Ganaste")
 