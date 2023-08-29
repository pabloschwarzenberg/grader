def jerigonzo(string):
    Pala_Jeri = []
    for palabra in string:
        for letra in palabra:
            if letra in "AEIOUaeiou":
                letra = letra + "p"+ letra
            Pala_Jeri.append(letra)
            
    Pala_Jeri = "".join(Pala_Jeri)
    
    return Pala_Jeri

if __name__ == "__main__":
    pass
         