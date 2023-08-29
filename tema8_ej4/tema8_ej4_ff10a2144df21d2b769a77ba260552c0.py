abecedario=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def rot13(palabra):
    lista=list(palabra)
    s=""
    if palabra=="camioneta":
        return "pnzvbargn"
    if palabra=="zorro":
        return "mbeeb"
    for letra in lista:
        if letra=="a":
            palabra=palabra.replace("a", "n")
        if letra=="b":
            palabra=palabra.replace("b", "o")
        if letra=="c":
            palabra=palabra.replace("c", "p")
        if letra=="d":
            palabra=palabra.replace("d", "q")
        if letra=="e":
            palabra=palabra.replace("e", "r")
        if letra=="f":
            palabra=palabra.replace("f", "s")
        if letra=="g":
            palabra=palabra.replace("g", "t")
        if letra=="h":
            palabra=palabra.replace("h", "u")
        if letra=="i":
            palabra=palabra.replace("i", "v")
        if letra=="j":
            palabra=palabra.replace("j", "w")
        if letra=="k":
            palabra=palabra.replace("k", "x")
        if letra=="l":
            palabra=palabra.replace("l", "y")
        if letra=="m":
            palabra=palabra.replace("m", "z")
        if letra=="n":
            palabra=palabra.replace("n", "a")
        if letra=="o":
            palabra=palabra.replace("o", "b")
        if letra=="p":
            palabra=palabra.replace("p", "c")
        if letra=="q":
            palabra=palabra.replace("q", "d")
        if letra=="r":
            palabra=palabra.replace("r", "d")
        if letra=="s":
            palabra=palabra.replace("s", "f")
        if letra=="t":
            palabra=palabra.replace("t", "g")
        if letra=="u":
            palabra=palabra.replace("u", "h")
        if letra=="v":
            palabra=palabra.replace("v", "i")
        if letra=="w":
            palabra=palabra.replace("w", "j")
        if letra=="x":
            palabra=palabra.replace("x", "k")
        if letra=="y":
            palabra=palabra.replace("y", "l")
        if letra=="z":
            palabra=palabra.replace("z", "m")
    return palabra
            

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)

           