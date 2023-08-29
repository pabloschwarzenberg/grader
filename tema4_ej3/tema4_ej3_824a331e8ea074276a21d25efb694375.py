def jerigonzo(texto):
    vocal=["a","e","i","o","u","A","E","I","O","U"]
    jeri=[]
    nueva=""
    for i in texto:
        jeri.append(i)      
        if i in vocal:
            jeri.append("p")
            jeri.append(i)
            
    for k in jeri:
          nueva=nueva+str(k)    
    
    return nueva
