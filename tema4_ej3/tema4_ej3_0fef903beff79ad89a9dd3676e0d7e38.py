def jerigonzo(string):
    jeri=""
    for x in string:
        if x in "aeiou":
            jeri=jeri+x
            jeri=jeri+"p"
        jeri=jeri+x
    return jeri
