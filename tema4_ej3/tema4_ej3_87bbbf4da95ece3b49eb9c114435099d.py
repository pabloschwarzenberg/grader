def jerigonzo(a):
    palabravacia = ""
    for c in a:
        palabravacia += c
        if c in "AEIOUaeiou":
            palabravacia += "p"
            palabravacia += c

    return palabravacia
