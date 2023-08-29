def rot13(palabra):
    palabra=palabra.lower()
    palabra=list(palabra)
    palabra2=list(palabra)


    for i in range(len(palabra)):
        if palabra[i]=="a":
            palabra2.pop(i)
            palabra2.insert(i,"n")
            
        if palabra[i]=="b":
            palabra2.pop(i)
            palabra2.insert(i,"o")
            
        if palabra[i]=="c":
            palabra2.pop(i)
            palabra2.insert(i,"p")
            
        if palabra[i]=="d":
            palabra2.pop(i)
            palabra2.insert(i,"q")
            
        if palabra[i]=="e":
            palabra2.pop(i)
            palabra2.insert(i,"r")

        if palabra[i]=="f":
            palabra2.pop(i)
            palabra2.insert(i,"s")            

        if palabra[i]=="g":
            palabra2.pop(i)
            palabra2.insert(i,"t")

        if palabra[i]=="h":
            palabra2.pop(i)
            palabra2.insert(i,"u")

        if palabra[i]=="i":
            palabra2.pop(i)
            palabra2.insert(i,"v")

        if palabra[i]=="j":
            palabra2.pop(i)
            palabra2.insert(i,"w")

        if palabra[i]=="k":
            palabra2.pop(i)
            palabra2.insert(i,"x")

        if palabra[i]=="l":
            palabra2.pop(i)
            palabra2.insert(i,"y")                

        if palabra[i]=="m":
            palabra2.pop(i)
            palabra2.insert(i,"z")

        if palabra[i]=="n":
            palabra2.pop(i)
            palabra2.insert(i,"a")

        if palabra[i]=="o":
            palabra2.pop(i)
            palabra2.insert(i,"b")

        if palabra[i]=="p":
            palabra2.pop(i)
            palabra2.insert(i,"c")

        if palabra[i]=="q":
            palabra2.pop(i)
            palabra2.insert(i,"d")

        if palabra[i]=="r":
            palabra2.pop(i)
            palabra2.insert(i,"e")

        if palabra[i]=="s":
            palabra2.pop(i)
            palabra2.insert(i,"f")

        if palabra[i]=="t":
            palabra2.pop(i)
            palabra2.insert(i,"g")

        if palabra[i]=="u":
            palabra2.pop(i)
            palabra2.insert(i,"h")

        if palabra[i]=="v":
            palabra2.pop(i)
            palabra2.insert(i,"i")

        if palabra[i]=="w":
            palabra2.pop(i)
            palabra2.insert(i,"j")

        if palabra[i]=="x":
            palabra2.pop(i)
            palabra2.insert(i,"k")

        if palabra[i]=="y":
            palabra2.pop(i)
            palabra2.insert(i,"l")

        if palabra[i]=="z":
            palabra2.pop(i)
            palabra2.insert(i,"m")

    return "".join(palabra2)


if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
  
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           