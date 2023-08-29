def levenshtein(a,b):
    listaA=[]
    listaB=[]
    lista1=[]
    i=0
    j=0
    k=0
    m=0
    while i<len(a):
        listaA.append(a[i])
        i=i+1
    while j<len(b):
        listaB.append(b[j])
        j=j+1
    if len(a)==len(b):
        while m<len(a):
            if listaA[m]!=listaB[m]:
                lista1.append(listaA[m])
            m=m+1
    print(listaA,listaB,lista1,len(a),len(b))
    if a==b:
        return "0D"
        
    elif len(a)>len(b) and len(a)+1!=len(b):
        return "+1"
    elif len(a)<len(b) and len(a)+1!=len(b):
        return "+1"
    elif len(lista1)==1:
        return "1S"
    elif len(a)+1==len(b) or len(a)-1==b or len(a)==len(b)+1 or len(a)==len(b)-1:
        return "IB"
    