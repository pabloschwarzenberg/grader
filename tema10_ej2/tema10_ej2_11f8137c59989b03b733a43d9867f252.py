def levenshtein(palabra1,palabra2):
    b=0
    w=0
    c=0
    if len(palabra1)<len(palabra2):
                         r=palabra1
                         q=palabra2
    else:
                         r=palabra2
                         q=palabra1
                         
                         
    
         
    for i in r:         #Para ver si hay que agregar o quitar letras
        if w>len(r):
            break
             
        if r[w]!=q[c]:
            b=b-1
            if len(r)!=len(q):
                w=w
            if len(r)==len(q):
                w=w+1
            c=c+1
        
        else:
            w=w+1
            c=c+1

    if b<-1 or abs(len(palabra1)-len(palabra2))>1:
        return'+1'
        
    elif abs(len(palabra1)-len(palabra2))==1 and b==-1: 
        return'IB'

    elif len(palabra1)==len(palabra2) and b==-1:
        return'1S'

    elif b==0 and len(palabra1)==len(palabra2):
        return'0D'



if __name__=="__main__":
    pass
           