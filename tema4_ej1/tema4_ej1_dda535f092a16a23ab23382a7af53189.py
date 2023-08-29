
    palabras = ["lepidoptero", "mariposa", "elefante", "computadora", "python"]
    palabra_secreta = seleccionar_palabra(palabras)
    print("Palabra secreta: ", palabra_secreta)
    palabra_oculta = ocultar_letras(palabra_secreta, 3)
    print("Palabra oculta: ", palabra_oculta)

    while "_" in palabra_oculta:
        letra = input("Ingresa una letra: ")
        palabra_oculta = revisar_letra(palabra_secreta,palabra_oculta,letra)
        print("Palabra: ",palabra_oculta)

    print("¡Has adivinado la palabra!")