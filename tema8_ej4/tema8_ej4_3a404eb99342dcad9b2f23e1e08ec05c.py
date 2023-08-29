def rot13(palabra):
    palabra=palabra.replace("a","x")
    palabra=palabra.replace("n","a")
    palabra=palabra.replace("x","n")
    
    palabra=palabra.replace("b","x")
    palabra=palabra.replace("o","b")
    palabra=palabra.replace("x","o")
    
    palabra=palabra.replace("c","x")
    palabra=palabra.replace("p","c")
    palabra=palabra.replace("x","p")
    
    palabra=palabra.replace("d","x")
    palabra=palabra.replace("q","d")
    palabra=palabra.replace("x","q")

    palabra=palabra.replace("e","x")
    palabra=palabra.replace("r","e")
    palabra=palabra.replace("x","r")
    
    palabra=palabra.replace("f","x")
    palabra=palabra.replace("s","f")
    palabra=palabra.replace("x","s")
    
    palabra=palabra.replace("g","x")
    palabra=palabra.replace("t","g")
    palabra=palabra.replace("x","t")
    
    palabra=palabra.replace("h","x")
    palabra=palabra.replace("u","h")
    palabra=palabra.replace("x","u")
    
    palabra=palabra.replace("i","x")
    palabra=palabra.replace("v","i")
    palabra=palabra.replace("x","v")
    
    palabra=palabra.replace("j","x")
    palabra=palabra.replace("w","j")
    palabra=palabra.replace("x","w")
    
    palabra=palabra.replace("k","y")
    palabra=palabra.replace("x","k")
    palabra=palabra.replace("y","x")
    
    palabra=palabra.replace("l","x")
    palabra=palabra.replace("y","l")
    palabra=palabra.replace("x","y")
    
    palabra=palabra.replace("m","x")
    palabra=palabra.replace("z","m")
    palabra=palabra.replace("x","z")

    return palabra

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)


           