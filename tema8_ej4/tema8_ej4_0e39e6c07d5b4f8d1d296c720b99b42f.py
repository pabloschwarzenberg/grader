def rot13(a):
    abc =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    largo=len(a)
    for o in range(0,largo):
        posicion=abc.index(a[o])
        if posicion<=12:
           c=a[o]
           b=abc[posicion+13]
           s=list(a)
           s.pop(o)
           s.insert(o,b)
           print(s)
           a="".join(s)
        elif posicion>=13:
           c=a[o]
           b=abc[posicion-13]
           s=list(a)
           s.pop(o)
           s.insert(o,b)
           print(s)
           a="".join(s)
    return(a)
          
      

        
           