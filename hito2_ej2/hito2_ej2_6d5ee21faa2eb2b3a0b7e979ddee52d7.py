def genomafunc() :
    genoma = input("Ingrese el genoma")
    cont = 0
    for gen in genoma :
        if gen[cont].lower() != "a" or gen[cont].lower() != "c" or gen[cont].lower() != "t" or gen[cont].lower() != "g" :
            return "la secuencia " + genoma + " es incorrecta"
        cont = cont + 1
    return "la secuencia " + genoma + " es correcta"

print(genomafunc())
    
    