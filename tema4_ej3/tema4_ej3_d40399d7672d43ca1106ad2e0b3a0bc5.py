def jerigonzo(string):
    jeri_str = ""

    for vocal in string.lower():
        if vocal in "aeiouáéíóúü":
            jeri_str += vocal
            jeri_str += "p"

        jeri_str += vocal
    
    return jeri_str