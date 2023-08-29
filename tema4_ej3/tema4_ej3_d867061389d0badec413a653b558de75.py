def jerigonzo(string):
    texto=[]
    voc=["a","e","i","o","u"]
    cons=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
    for letra in string:
        if letra in voc:
            texto+=letra+"p"+letra
        if letra in cons:
            texto+=letra
        if letra==" ":
            texto+=" "
        string="".join(texto)
    return string

if __name__ == "__main__":
    pass
         