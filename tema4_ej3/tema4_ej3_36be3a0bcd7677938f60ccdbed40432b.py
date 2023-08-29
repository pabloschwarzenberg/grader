def jerigonzo(string):
    nuevotxt = ""
    for palabra in string:
        for letra in range(len(palabra)):
            if palabra[letra] in "aeiouAEIOU":
                antigua = palabra[letra]
                antiguap = palabra[letra] + "p" + antigua
            else:
                antiguap = palabra[letra]
        
            nuevotxt += antiguap

    return nuevotxt
         