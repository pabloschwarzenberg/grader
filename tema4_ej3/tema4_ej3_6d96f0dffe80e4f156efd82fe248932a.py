def jerigonzo(string):
    Texto= ""
    for i in range(len(string)):
        Texto = Texto + string[i]
        if string[i] in "aeiouAEIOU":
            Texto= Texto + "p" + string[i]        
    return Texto
    pass      