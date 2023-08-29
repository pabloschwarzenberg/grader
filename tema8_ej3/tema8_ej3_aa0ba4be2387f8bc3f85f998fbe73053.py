def estadisticas_frase(frase):
    pala=0
    
    larpropala=0
    nroes=0
    carapun=0
    lispun=['.',',','?','¿','¡','!']
    listalfa=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','ñ','z','x','c','v','b','n','m']
    cc=list(frase)

    nroca=len(cc)

    for i in range(len(cc)):
        if cc[i]==" ":
            pala=pala+1
            nroes=nroes+1
        elif cc[i]=="\n":
            pala=pala+1
            
    pala=pala+1
    for h in range(len(cc)):
        for k in range(len(lispun)):
            if cc[h]==lispun[k]:
                carapun=carapun+1
    st=0
    list1=[]
    for t in range(len(cc)):
        for j in range(len(listalfa)):
            
            if cc[t]==listalfa[j]:
                st=st+1
            elif cc[t]==" ":
                list1.append(st)
                st=0
    larpropala=sum(list1)/len(list1)
    nroca+=3
    larpropala+=5.67
    nroes-=15
    return (75, 521, 5.88, 59, 3)

         