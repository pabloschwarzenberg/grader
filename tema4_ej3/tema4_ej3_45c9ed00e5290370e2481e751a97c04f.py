def jerigonzo(palabra):
    nueva_palabra = ""

    for letra in palabra:
        if letra in "AEIOUaeiouáéíóúÄËÏÖÜäëïöü":
            nueva_palabra += letra+ "p"
        
        nueva_palabra += letra
    return nueva_palabra