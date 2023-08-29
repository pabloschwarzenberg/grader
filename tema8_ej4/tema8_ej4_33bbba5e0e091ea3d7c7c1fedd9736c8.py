def rot13(palabra):
    rot13 = []
    alfabeto= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in palabra:
        letra = alfabeto.index(i)
        letra_rot13 = (alfabeto[letra -13])
        rot13.append(letra_rot13)

    return("".join(rot13))           