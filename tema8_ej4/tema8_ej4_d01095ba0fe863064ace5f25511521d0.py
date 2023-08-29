def rot13(palabra):
    palabra_lista=list(palabra)
    lista_rot13=[]
    for i in range(len(palabra_lista)):
        if palabra_lista(i)=="a":
           lista_rot13.append("n")
        if palabra_lista(i)=="b":
           lista_rot13.append("o")
        if palabra_lista(i)=="c":
           lista_rot13.append("p")
        if palabra(i)=="d":
           lista_rot13.append("q")           
        if palabra(i)=="e":
           lista_rot13.append("r")        
        if palabra(i)=="f":
           lista_rot13.append("s")
        if palabra(i)=="g":
           lista_rot13.append("t")           
        if palabra(i)=="h":
           lista_rot13.append("u")           
        if palabra(i)=="i":
           lista_rot13.append("v")           
        if palabra(i)=="j":
           lista_rot13.append("w")           
        if palabra(i)=="k":
           lista_rot13.append("x")           
        if palabra(i)=="l":
           lista_rot13.append("y")           
        if palabra(i)=="m":
           lista_rot13.append("z")           
        if palabra(i)=="n":
           lista_rot13.append("a")           
        if palabra(i)=="o":
           lista_rot13.append("b")
        if palabra(i)=="p":
           lista_rot13.append("c") 
        if palabra(i)=="q":
           lista_rot13.append("d") 
        if palabra(i)=="r":
           lista_rot13.append("e") 
        if palabra(i)=="s":
           lista_rot13.append("f") 
        if palabra(i)=="t":
           lista_rot13.append("g") 
        if palabra(i)=="u":
           lista_rot13.append("h") 
        if palabra(i)=="v":
           lista_rot13.append("i") 
        if palabra(i)=="w":
           lista_rot13.append("j")    
        if palabra(i)=="x":
           lista_rot13.append("k")
        if palabra(i)=="y":
           lista_rot13.append("l")
        if palabra(i)=="z":
           lista_rot13.append("m")
    palabra_final="".join(lista_rot13)
    return palabra_final
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           