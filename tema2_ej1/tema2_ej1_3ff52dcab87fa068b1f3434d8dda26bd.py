def areatriangulo(base,altura):
    cal=(base*altura)/2
    return cal
def arearombo(diagonalA,diagonalB):
    cal=(diagonalA*diagonalB)/2
    return cal
def arearectangulo(largo,ancho):
    cal=largo*ancho
    return cal
def areacirculo(radio):
    cal=3.14*radio**2
    return cal
def procesaopciones(opcion):
    if opcion == 1:
        radio=float(input('ingresa el radio: '))
        área=areacirculo(radio)
    elif opcion == 2:
        largo=float(input('ingresa el largo: '))
        ancho=float(input('ingresa el ancho: '))
        área=arearectangulo(largo,ancho)
    elif opcion == 3:
        diagonalA=float(input('ingresa el diagonalA: '))
        diagonalB=float(input('ingresa el diagonalB: '))
        área=arearombo(diagonalA,diagonalB)
    elif opcion == 4:
        base=float(input('ingresa la base: '))
        altura=float(input('ingresa la altura: '))
        área=areatriangulo(base,altura)
    if opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4:
        print('el area es: ', área)
        
def Menu():
    opcion=1
    while opcion!=5:
        print("\n                MENU")
        print("")
        print("          1. ÁREA CÍRCULO")
        print("          2. ÁREA RECTÁNGULO")
        print("          3. ÁREA CUADRADO")
        print("          4. ÁREA TRIÁNGULO")
        print("          5. SALIR")
        print("")
        opcion=int(input('ingresa la opcion que deseas: '))
        procesaopciones(opcion)
Menu()

