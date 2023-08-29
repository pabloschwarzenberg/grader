def jerigonzo(string):
    texto= str("")
    for vocal in string:
        if vocal in ("aeiou"):
            texto += vocal
            texto += "p"
        texto += vocal
    
    return texto