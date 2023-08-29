def jerigonzo(string):
    Vocales= ["a","e","i","o","u"]
    Lista_str = list(str(string).lower())
    nuevo_str=[]
    for largo in range(len(Lista_str)):
        if Lista_str[largo] in Vocales:
            nuevo_str.append(str(Lista_str[largo]+"p"+Lista_str[largo]))
        else:
            nuevo_str.append(str(Lista_str[largo]))
    return "".join(nuevo_str)