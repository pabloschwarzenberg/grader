def rot13(palabra):
    i=0
    cuenta=""

    while i<(len(palabra)):

        if palabra[i]==("a"):
            a=palabra[i].replace("a","n")
            cuenta=cuenta+str(a)
        elif palabra[i]==("b"):
            b=palabra[i].replace("b","o")
            cuenta=cuenta+str(b)
        elif palabra[i]==("c"):
            c=palabra[i].replace("c","p")
            cuenta=cuenta+str(c)
        elif palabra[i]==("d"):
            d=palabra[i].replace("d","q")
            cuenta=cuenta+str(d)
        elif palabra[i]==("e"):
            e=palabra[i].replace("e","r")
            cuenta=cuenta+str(e)
        elif palabra[i]==("f"):
            f=palabra[i].replace("f","s")
            cuenta=cuenta+str(f)
        elif palabra[i]==("g"):
            g=palabra[i].replace("g","t")
            cuenta=cuenta+str(g)
        elif palabra[i]==("h"):
            h=palabra[i].replace("h","u")
            cuenta=cuenta+str(h)
        elif palabra[i]==("i"):
            i2=palabra[i].replace("i","v")
            cuenta=cuenta+str(i2)
        elif palabra[i]==("j"):
            j=palabra[i].replace("j","w")
            cuenta=cuenta+str(j)
        elif palabra[i]==("k"):
            k=palabra[i].replace("k","x")
            cuenta=cuenta+str(k)
        elif palabra[i]==("l"):
            l=palabra[i].replace("l","y")
            cuenta=cuenta+str(l)
        elif palabra[i]==("m"):
            m=palabra[i].replace("m","z")
            cuenta=cuenta+str(m)
        elif palabra[i]==("n"):
            n=palabra[i].replace("n","a")
            cuenta=cuenta+str(n)
        elif palabra[i]==("o"):
            o=palabra[i].replace("o","b")
            cuenta=cuenta+str(o)
        elif palabra[i]==("p"):
            p=palabra[i].replace("p","c")
            cuenta=cuenta+str(p)
        elif palabra[i]==("q"):
            q=palabra[i].replace("q","d")
            cuenta=cuenta+str(q)
        elif palabra[i]==("r"):
            r=palabra[i].replace("r","e")
            cuenta=cuenta+str(r)
        elif palabra[i]==("s"):
            s=palabra[i].replace("s","f")
            cuenta=cuenta+str(s)
        elif palabra[i]==("t"):
            t=palabra[i].replace("t","g")
            cuenta=cuenta+str(t)
        elif palabra[i]==("u"):
            u=palabra[i].replace("u","h")
            cuenta=cuenta+str(u)
        elif palabra[i]==("v"):
            v=palabra[i].replace("v","i")
            cuenta=cuenta+str(v)
        elif palabra[i]==("w"):
            w=palabra[i].replace("w","j")
            cuenta=cuenta+str(w)
        elif palabra[i]==("x"):
            x=palabra[i].replace("x","k")
            cuenta=cuenta+str(x)
        elif palabra[i]==("y"):
            y=palabra[i].replace("y","l")
            cuenta=cuenta+str(y)
        elif palabra[i]==("z"):
            z=palabra[i].replace("z","m")
            cuenta=cuenta+str(z)

        i=i+1 

    return(cuenta)
    
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           