   
def rot13(palabra):
    a=palabra.replace("n","N")
    b=a.replace("a","n")
    c=b.replace("N","a")
    d=c.replace("o","O")
    e=d.replace("b","o")
    f=e.replace("O","b")
    g=f.replace("p","P")
    h=g.replace("c","p")
    i=h.replace("P","c")
    j=i.replace("q","Q")
    k=j.replace("d","q")
    l=k.replace("Q","d")
    m=l.replace("r","R")
    n=m.replace("e","r")
    o=n.replace("R","e")
    p=o.replace("s","S")
    q=p.replace("f","s")
    r=q.replace("S","f")
    s=r.replace("t","T")
    t=s.replace("g","t")
    u=t.replace("T","g")
    v=u.replace("u","U")
    w=v.replace("h","u")
    x=w.replace("U","h")
    y=x.replace("v","V")
    z=y.replace("i","v")
    a1=z.replace("V","i")
    b1=a1.replace("w","W")
    c1=b1.replace("j","w")
    d1=c1.replace("W","j")
    e1=d1.replace("x","X")
    f1=e1.replace("k","x")
    g1=f1.replace("X","k")
    h1=g1.replace("y","Y")
    i1=h1.replace("l","y")
    j1=i1.replace("Y","l")
    k1=j1.replace("z","Z")
    l1=k1.replace("m","z")
    resultado=l1.replace("Z","m")
    
    return resultado
    

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           