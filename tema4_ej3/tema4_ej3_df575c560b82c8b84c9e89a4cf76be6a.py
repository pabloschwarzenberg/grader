def jerigonzo(a):
    z = "aeiou"
    t = ""
    for letra in a:
        if letra in z:
            t = t + letra + "p" + letra
        else:
            t = t + letra
    return t

if __name__ == "__main__":
    a = input()
    print(jerigonzo(a))
    
         