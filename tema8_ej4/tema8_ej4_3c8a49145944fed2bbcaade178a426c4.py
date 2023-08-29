def rot13(s):
    p=""
    s=s.lower()
    for letra in s:
        if letra=="a":
            c= letra.replace("a","n")
            p= p+c
        if letra=="b":
            c=letra.replace("b","o")
            p= p+c
        if letra=="c":
            c=letra.replace("c","p")
            p= p+c
        if letra=="d":
            c=letra.replace("d","q")
            p= p+c
        if letra=="e":
            c=letra.replace("e","r")
            p= p+c
        if letra=="f":
            c=letra.replace("f","s")
            p= p+c
        if letra=="g":
            c=letra.replace("g","t")
            p= p+c
        if letra=="h":
            c=letra.replace("h","u")
            p= p+c
        if letra=="i":
            c=letra.replace("i","v")
            p= p+c
        if letra=="j":
            c=letra.replace("j","w")
            p= p+c
        if letra=="k":
            c=letra.replace("k","x")
            p= p+c
        if letra=="l":
            c=letra.replace("l","y")
            p= p+c
        if letra=="m":
            c=letra.replace("m","z")
            p= p+c
        if letra=="n":
            c= letra.replace("n","a")
            p= p+c
        if letra=="o":
            c=letra.replace("o","b")
            p= p+c
        if letra=="p":
            c=letra.replace("p","c")
            p= p+c
        if letra=="q":
            c=letra.replace("q","d")
            p= p+c
        if letra=="r":
            c=letra.replace("r","e")
            p= p+c
        if letra=="s":
            c=letra.replace("s","f")
            p= p+c
        if letra=="t":
            c=letra.replace("t","g")
            p= p+c
        if letra=="u":
            c=letra.replace("u","h")
            p= p+c
        if letra=="v":
            c=letra.replace("v","i")
            p= p+c
        if letra=="w":
            c=letra.replace("w","j")
            p= p+c
        if letra=="x":
            c=letra.replace("x","k")
            p= p+c
        if letra=="y":
            c=letra.replace("y","l")
            p= p+c
        if letra=="z":
            c=letra.replace("z","m")
            p= p+c
    return p

if __name__=="__main__":
    s= input("Ingrese palabra a encriptar: ")
    print("Aqui esta tu palabra encriptada: "+str(rot13(s)))
           