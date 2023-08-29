def rot13(palabra):
    x=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    w=["n","o","p","q","r","s","t","u","v","w","x","y","z"]
    z=""
    for y in palabra:
        if y in x:
            for i in range(0,len(x)):
                if (x[i]==y):
                    y=w[i]
        else:
            for i in range(0,len(w)):
                if (w[i]==y):
                    y=x[i]
        z=z+y
        
    return z
           