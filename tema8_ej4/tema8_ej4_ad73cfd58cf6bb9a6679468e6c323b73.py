def rot13(palabra):
    l=['a','b','c','d','e','f','g','h','i','j',
       'k','l','m','n','o','p','q','r','s','t',
       'u','v','w','x','y','z']
    frase=''
    i=0
    j=0
    palabra=palabra.lower()
    while i< len(palabra):
        x= palabra[i]
        if x ==l[j]:
            if l[j]>='n':
                t=x.replace(x,l[j-13])
                frase=frase+t
                i=i+1
            else:
                t= x.replace(x,l[j+13])
                frase=frase+t
                i=i+1    
        j=j+1
        if j==26:
            j=0
        
    return frase
           