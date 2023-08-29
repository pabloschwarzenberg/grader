def jerigonzo(string):
    miPalabra=""
    letras=["a","e","i","o","u"]
    for i in (string):
        if i not in letras:  
            miPalabra+=i
            
        else:
            miPalabra+=i
            miPalabra+="p"
            miPalabra+=i

    return miPalabra

if __name__ == "__main__":
    pass
         