import math
def levenshtein(palabra1,palabra2):
    letras_a=[]
    letras_b=[]
    letras_c=[]
    if len(palabra1)>len(palabra2):
        for i in palabra2:
            a=palabra1.find(i)
            letras_a.append(str(a))
            while "-1"in letras_a:
                letras_a.remove("-1")
        distancia=(len(palabra1))-(len(letras_a))
        print(letras_a)
        if distancia>1:
            return "+1"
        elif distancia==1:
            return "IB"
    elif len(palabra1)<len(palabra2):
        for k in palabra1:
            b=palabra2.find(k)
            letras_b.append(str(b))
            while "-1"in letras_b:
                letras_b.remove("-1")
        distancia=(len(palabra2))-(len(letras_b))
        if distancia>1:
            return "+1"
        elif distancia==1:
            return "IB"
    elif len(palabra1)==len(palabra2):
        if palabra1==palabra2:
            return "0D"
        else:
            return "1S"
    
                                
                        
if __name__=="__main__":
    print(levenshtein("gato","gatito"))
    print(levenshtein("hola","ola"))
    print(levenshtein("gallina","gallina"))
    print(levenshtein("caro","cara"))
    print(levenshtein("carajo","carajito"))
    print(levenshtein("jarron","melon"))
           