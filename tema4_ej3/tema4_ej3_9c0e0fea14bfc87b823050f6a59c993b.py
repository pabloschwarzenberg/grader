def jerigonzo(a):
    palabra= ""
    for vocal in a:
        if vocal in "AEIOUaeiou":
            palabra += vocal
            palabra += "p"
        palabra += vocal
    return palabra
         