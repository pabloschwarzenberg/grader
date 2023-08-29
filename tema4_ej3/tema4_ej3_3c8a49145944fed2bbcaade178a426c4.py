def jerigonzo(s):
    a = "a"
    e="e"
    i="i"
    o="o"
    u="u"
    p=""
    for letra in s:
        if letra=="a":
            c= letra.replace("a","apa")
            p= p+c
        if letra=="e":
            c=letra.replace("e","epe")
            p= p+c
        if letra=="i":
            c=letra.replace("i","ipi")
            p= p+c
        if letra=="o":
            c=letra.replace("o","opo")
            p= p+c
        if letra=="u":
            c=letra.replace("u","upu")
            p= p+c
        if letra not in (a,e,i,o,u):
            p= p+letra
    return p

if __name__ == "__main__":
    s= str(input("Ingresa palabra para transformarla en jerigonzio!: "))
    print("Tu palabra transformada es: "+str(jerigonzo(s)))
         