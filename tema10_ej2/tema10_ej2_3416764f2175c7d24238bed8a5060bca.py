def levenshtein(palabra1,palabra2):

    largo1=len(palabra1)
    largo2=len(palabra2)

    x=list(palabra1)
    y=list(palabra2)

    hola='+1'
    holasin= hola.replace("'","")

    que='0D'
    quesin=que.replace("'","")

    estas='IB'
    estassin=estas.replace("'","")

    haciendo='1S'
    haciendosin=haciendo.replace("'","")

    if (largo1-largo2)>1:
        return holasin

    if (largo2-largo1)>1:
        return holasin
    
    if palabra1==palabra2:
        return quesin

    if (largo1-largo2)==1:
        return estassin

    if (largo2-largo1)==1:
        return estassin

    if (largo1-largo2)==0:
        i=0
        cont=0
        while x[i]==y[i]:
            i=i+1
            cont=cont+1
            
        if x[i]!=y[i]:        
            return haciendosin

    if (largo2-largo1)==0:
        i=0
        cont=0
        while x[i]==y[i]:
            i=i+1
            cont=cont+1
            
        if x[i]!=y[i]:        
            return haciendosin
     