def rot13(palabra):
    c=len(palabra)
    oracion=[]
    p=""
    for d in range (c):
        nu=palabra[d]
        cambios=0
        if nu=="a" and cambios!=1:
            nu=nu.replace("a","n")
            cambios=1
        if nu=="n" and cambios!=1:
            nu=nu.replace("n","a")
            cambios=1
        if nu=="b" and cambios!=1:
            nu=nu.replace("b","o")
            cambios=1
        if nu=="c" and cambios!=1:
            nu=nu.replace("c","p")
            cambios=1
        if nu=="d" and cambios!=1:
            nu=nu.replace("d","q")
            cambios=1
        if nu=="e" and cambios!=1:
            nu=nu.replace("e","r")
            cambios=1
        if nu=="f" and cambios!=1:
            nu=nu.replace("f","s")
            cambios=1
        if nu=="g" and cambios!=1:
            nu=nu.replace("g","t")
            cambios=1
        if nu=="h" and cambios!=1:
            nu=nu.replace("h","u")
            cambios=1
        if nu=="i" and cambios!=1:
            nu=nu.replace("i","v")
            cambios=1
        if nu=="j" and cambios!=1:
            nu=nu.replace("j","w")
            cambios=1
        if nu=="k" and cambios!=1:
            nu=nu.replace("k","x")
            cambios=1
        if nu=="l" and cambios!=1:
            nu=nu.replace("l","y")
            cambios=1
        if nu=="m" and cambios!=1:
            nu=nu.replace("m","z")
            cambios=1
        if nu=="o" and cambios!=1:
            nu=nu.replace("o","b")
            cambios=1
        if nu=="p" and cambios!=1:
            nu=nu.replace("p","c")
            cambios=1
        if nu=="q" and cambios!=1:
            nu=nu.replace("q","d")
            cambios=1
        if nu=="r" and cambios!=1:
            nu=nu.replace("r","e")
            cambios=1
        if nu=="s" and cambios!=1:
            nu=nu.replace("s","f")
            cambios=1
        if nu=="t" and cambios!=1:
            nu=nu.replace("t","g")
            cambios=1
        if nu=="u" and cambios!=1:
            nu=nu.replace("u","h")
            cambios=1
        if nu=="v" and cambios!=1:
            nu=nu.replace("v","i")
            cambios=1
        if nu=="w" and cambios!=1:
            nu=nu.replace("w","j")
            cambios=1
        if nu=="x" and cambios!=1:
            nu=nu.replace("x","k")
            cambios=1
        if nu=="y" and cambios!=1:
            nu=nu.replace("y","l")
            cambios=1
        if nu=="z" and cambios!=1:
            nu=nu.replace("z","m")
            cambios=1
        oracion.append(nu)
    for o in range(c):
        p=p+oracion[o]
    palabra=p
    return palabra

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           