def rot13(palabra):
    i=0
    palabra_codificada=palabra
    while i<=len(palabra):
        if palabra[i]==palabra_codificada[i]:
            palabra_codificada=palabra.replace("a","n")
            palabra_codificada=palabra.replace("b","o")
            palabra_codificada=palabra.replace("c","p")
            palabra_codificada=palabra.replace("d","q")
            palabra_codificada=palabra.replace("e","r")
            palabra_codificada=palabra.replace("f","s")
            palabra_codificada=palabra.replace("g","t")
            palabra_codificada=palabra.replace("h","u")
            palabra_codificada=palabra.replace("i","v")
            palabra_codificada=palabra.replace("j","w")
            palabra_codificada=palabra.replace("k","x")
            palabra_codificada=palabra.replace("l","y")
            palabra_codificada=palabra.replace("m","z")
            palabra_codificada=palabra.replace("n","a")
            palabra_codificada=palabra.replace("o","b")
            palabra_codificada=palabra.replace("p","c")
            palabra_codificada=palabra.replace("q","d")
            palabra_codificada=palabra.replace("r","e")
            palabra_codificada=palabra.replace("s","f")
            palabra_codificada=palabra.replace("t","g")
            palabra_codificada=palabra.replace("u","h")
            palabra_codificada=palabra.replace("v","i")
            palabra_codificada=palabra.replace("w","j")
            palabra_codificada=palabra.replace("x","k")
            palabra_codificada=palabra.replace("y","l")
            palabra_codificada=palabra.replace("z","m")
            i+=1
        else:
            i+=1
            continue
    return palabra_codificada


if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           