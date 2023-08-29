def jerigonzo(string):
    texto=""
    for i in string:
        if i == "a":
            texto+=i
            texto+="p"
        if i == "e":
            texto+=i
            texto+="p"
        if i == "i":
            texto+=i
            texto+="p"
        if i == "o":
            texto+=i
            texto+="p"
        if i == "u":
            texto+=i
            texto+="p"
        texto+=i
    return texto