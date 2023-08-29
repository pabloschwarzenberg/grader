def jerigonzo(texto):
    vocal=['a','e','i','o','u']
    txt=""
    for i in texto:
        if i in vocal:
            i=i+"p"+i
        txt+=i
    return(txt)
        
