def jerigonzo(string):
    listaPalabra = list(string)
    palabraJerigonzo = ""
    vocales = ["a", "e", "i", "o", "u"]


    for item in listaPalabra:
        esVocal = False
        for vocal in vocales:
            if item == vocal:
                palabraJerigonzo += item+"p"+item
                esVocal = True
                break

        if not esVocal:
           palabraJerigonzo += item

    return palabraJerigonzo