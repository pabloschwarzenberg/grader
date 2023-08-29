def rot13(palabra):
    alfa=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    alfas="".join(alfa)
    v=list(palabra)
    for letra in palabra:
        for abc in alfas:
            if letra==abc:
                posabc=alfas.find(abc)    
                cantletra=palabra.count(letra)
                i=0
                while i<=len(palabra):
                    posletra=palabra.find(letra,i,len(palabra))
                    if posletra>=0:
                        if posabc<=12:
                            v[posletra]=alfa[posabc+13]
                        elif posabc>12:
                            v[posletra]=alfa[posabc-13]
                    else: break
                    i=posletra+1
    rot13="".join(v)
    print(rot13)
    print(alfa[14])
    return(rot13)

           