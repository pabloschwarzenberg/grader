def rot13(palabra):
    parte1="abcdefghijklm"
    parte2="nopqrstuvwxyz"
    i=0
    L=[]
    while i<len(palabra):
        if palabra[i] in parte1:
            a=parte1.find(palabra[i])
            L.append(parte2[a])
        if palabra[i] in parte2:
            a=parte2.find(palabra[i])
            L.append(parte1[a])
        i+=1

    return ("".join(L))
    
            
          


        
           