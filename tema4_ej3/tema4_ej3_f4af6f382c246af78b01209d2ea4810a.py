def jerigonzo(string):
    vocales = "aeiou"
    jeri = "" 
    i = 0
    while i < len(string):
        if string[i] in vocales:
            jeri = jeri + string[i] + "p" + string[i]
        else:
            jeri = jeri + string[i]
        i+=1
    return jeri

if __name__ == "__main__":
    a = input()
    print(jerigonzo(a))
         