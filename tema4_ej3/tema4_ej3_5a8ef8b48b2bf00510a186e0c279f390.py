def jerigonzo(palabra):
    palabra_j =""
    for vocal in palabra:
        if vocal in "ÁÉÍÓÚAEIOUáéíóúaeiouÄäËëÏïÖöÜü":
            palabra_j += vocal
            palabra_j += "p"
        palabra_j += vocal
        
    return palabra_j