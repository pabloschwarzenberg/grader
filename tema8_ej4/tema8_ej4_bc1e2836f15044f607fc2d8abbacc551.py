def rot13(palabra):
    abc="abcdefghijklmnopqrstuvwxyz"
    abcd=list(abc)
    palabral=list(palabra)
    n=0
    for i in palabral:
       
       if i in abcd:  
           
           k=palabral.pop(n)
           r=abcd.index(k)
           if r<13:
               l=13+r
               efg=abcd.copy()
               q=efg.pop(l)
               palabral.insert(n,q)
               n+=1
           else:           
               l=r-13
               efg=abcd.copy()
               q=efg.pop(l)
               palabral.insert(n,q)
               n+=1
       else:
           n+=1
                      
       
    palabra="".join(palabral)
    return palabra
           