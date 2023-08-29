def estadisticas_frase(frase):
    largos=0
    enter=0
    vocales =0
    palabras=0
    espacios=0
    con=0
    s=0
    carpun=['.',',',';',':']
    c=['b','c','d','f','g','h','j','k','l','m','n','ñ','p','q','r','s','t','v','w','x','y','z','B','C','D','F','G','H','J','K','L','M','N','Ñ','P','Q','R','S','T','V','W','X','Y','Z']
    a=['a','e','i','o','u','A','E','I','O','U','á','é','í','ó','ú']
    for i in frase:
        if i in c:
            con=con+1
        elif i in a:
            vocales+=1
        elif i==' ':
            espacios+=1
        elif i=='\n':
            enter+=1
        else:
            s+=1
    
    palabras=espacios+1
    largo_promedio=(con+vocales+enter+s)/palabras
    return palabras,con+vocales+s+espacios+enter,largo_promedio,espacios,s
    