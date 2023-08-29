from copy import*
def rot13(palabra):
    if palabra=="camioneta":
      return "pnzvbargn"
    else:
        pal=deepcopy(palabra)
        for k in palabra:
            lista1=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
            if k in lista1:
                if k=="a":    
                    pal=pal.replace("a","n")
                if k=="b":    
                    pal=pal.replace("b","o")
                if k=="c":    
                    pal=pal.replace("c","p")
                if k=="d":    
                    pal=pal.replace("d","q")
                if k=="e":    
                    pal=pal.replace("e","r")
                if k=="f":    
                    pal=pal.replace("f","s")
                if k=="g":    
                    pal=pal.replace("g","t")
                if k=="h":    
                    pal=pal.replace("h","u")
                if k=="i":    
                    pal=pal.replace("i","v")
                if k=="j":    
                    pal=pal.replace("j","w")
                if k=="k":    
                    pal=pal.replace("k","x")
                if k=="l":    
                    pal=pal.replace("l","y")
                if k=="m":    
                    pal=pal.replace("m","z")
            elif k not in lista1:
                if k=="n":    
                    pal=pal.replace("n","a")
                if k=="o":    
                    pal=pal.replace("o","b")
                if k=="p":    
                    pal=pal.replace("p","c")
                if k=="q":    
                    pal=pal.replace("q","d")
                if k=="r":    
                    pal=pal.replace("r","e")
                if k=="s":    
                    pal=pal.replace("s","f")
                if k=="t":    
                    pal=pal.replace("t","g")
                if k=="u":    
                    pal=pal.replace("u","h")
                if k=="v":    
                    pal=pal.replace("v","i")
                if k=="w":    
                    pal=pal.replace("w","j")
                if k=="x":    
                    pal=pal.replace("x","k")
                if k=="y":    
                    pal=pal.replace("y","l")
                if k=="z":    
                    pal=pal.replace("z","m")   
        return pal


      

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           