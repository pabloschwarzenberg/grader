def validarsecuencias (secuencia):
    genoma = ["A", "C", "T", "G", "a", "c", "t", "g"]
    
    verificador = ""
    for a in secuencia:
        if a in genoma:
            verificador += a
        else:
            print("La secuencia ", secuencia, " es incorrecta")
            return
    
    print("La secuencia ", verificador, " es correcta")


secuencia = input("Ingrese una secuencia de letras: ")

validarsecuencias(secuencia)