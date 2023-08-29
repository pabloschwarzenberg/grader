def jerigonzo(a):
    a=a.lower()
    vocales=['a','e','i','o','u']
    a=list(a)
    nueva=[]
    for i in a:
        if i in vocales:
            i=i+"p"+i
            nueva.append(i)

        else:
            i=i
            nueva.append(i)
    nueva=''.join(nueva)
    return nueva

if __name__ == "__main__":
    pass
         