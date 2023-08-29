def rot13(palabra):
    abecedario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    abc="".join(abecedario)
    v=list(palabra)
    for letra in palabra:
        for alfa in abc:
             if letra==alfa:
                pos=abc.find(alfa)
                i=0
                while i<=len(palabra):
                    pos1=palabra.find(letra,i,len(palabra))
                    if 0<=pos1:
                        if pos<=12:
                            v[pos1]=abecedario[pos+13]
                        elif 12<pos:
                            v[pos1]=abecedario[pos-13]
                    else: break
                    i=pos1+1
    rot13="".join(v)
    print(rot13)
    return (rot13)
if __name__ == "__main__":               
  rot13(input())