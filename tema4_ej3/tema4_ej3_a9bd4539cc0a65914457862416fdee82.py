def vocal(letra):
    letra="AEIOUaeiouÁÉÍÓÚáéíóú"
def jerigonzo(string):
    aux=""
    for letra in string:
        if not vocal(letra):
            aux+=letra
        else:
            aux+=letra+"p"+letra
    
    return string

if __name__ == "__main__":
    pass
         