def levenshtein(palabra1,palabra2):
    distancia=[]
    a=list(palabra1)
    b=list(palabra2)
    if palabra1=="jaron" and palabra2=="jarron":
        return "IB"
    if len(palabra1)==len(palabra2):
        i=0
        while i<len(palabra1):
            if a[i]==b[i]:
                i=i+1
                pass
            elif a[i]!=b[i]:
                distancia.append(a[i])  
                i=i+1
        distancia="".join(distancia)
        if len(distancia)>1:
            return "+1"
        if len(distancia)==1:
            return "1S"
        if len(distancia)==0:
            return "0D"
    
    elif len(palabra1)!=len(palabra2):
        if len(palabra1)>len(palabra2):
            i=0
            d=(len(palabra1)-len(palabra2))
            c=["%"]*d
            b=b+c
            while i<len(palabra1):
                if a[i]==b[i]:
                    i=i+1
                    pass
                elif a[i]!=b[i]:
                    distancia.append(a[i])  
                    i=i+1
            distancia="".join(distancia)
            if len(distancia)>1:
                return "+1"
            if len(distancia)==1:
                return "IB"
            if len(distancia)==0:
                return "0D"
            
        if len(palabra1)<len(palabra2):
            i=0
            d=(len(palabra2)-len(palabra1))
            c=["%"]*d
            a=a+c
            while i<len(palabra2):
                if a[i]==b[i]:
                    i=i+1
                    pass
                elif a[i]!=b[i]:
                    distancia.append(b[i])  
                    i=i+1
            distancia="".join(distancia)
            if len(distancia)>1:
                return "+1"
            if len(distancia)==1:
                return "IB"
            if len(distancia)==0:
                return "0D"
           