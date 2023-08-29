def interpretar(expresion):
    a=0
    l=list(expresion)
    if "+" not in l and "-" not in l and "*" not in l and "/" not in l:
        return "".join(l)

    elif "*" in l:
        p=l.index("*")
        a=int(l[p-1])*int(l[p+1])
        l[p-1]=str(a)
        l=l[0:p]+l[p+2:]
        l="".join(l)
        print(l,"*")
        return interpretar(l)

    elif "/" in l:
        p=l.index("/")
        a=int(l[p-1])/int(l[p+1])
        l[p-1]=str(a)
        l=l[0:p]+l[p+2:]
        l="".join(l)
        print(l,"/")
        return interpretar(l)

    elif "+" in l:
        p=l.index("+")
        a=int(l[p-1])+int(l[p+1])
        l[p-1]=str(a)
        l=l[0:p]+l[p+2:]
        l="".join(l)
        print(l,"+")
        return interpretar(l)
        
    
    elif "-" in l:
        p=l.index("-")
        a=int(l[p-1])-int(l[p+1])
        l[p-1]=str(a)
        l=l[0:p]+l[p+2:]
        l="".join(l)
        return interpretar(l)
        
        
resultado=interpretar("2*3+5+6*7/9")
print(resultado)
#el resultado debiera ser 15.66666
 
#El programa falla cuando da como resultado un numero de dos cifras:/ 
#Sigo pensando en cómo arreglarlo