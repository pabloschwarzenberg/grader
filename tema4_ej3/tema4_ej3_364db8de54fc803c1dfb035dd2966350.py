def jerigonzo(word):
    new_word = ""
#para cada letra en "palabra"
    for letra in word:
        if letra in "AEIOUaeiou":
            new_word += letra+ "p"
#crear   
        new_word += letra
    return new_word