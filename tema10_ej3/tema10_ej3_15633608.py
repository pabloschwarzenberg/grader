def sopaletras(nombre_archivo,palabras):
    arc= open(nombre_archivo,"r")
    wowie=[]
    for j in arc:
        j=j.upper()
        a=j.replace("\n","")
        a=a.replace(" ","")
        b=list(a)
        wowie.append(b)
    wowa=[]
    for i in palabras:
        a=i.upper()
        a= list(a)
        b=None
        for e in a:

            for n in range(0,len(wowie)):
                for j in range(0,len(wowie[0])):
                    if e == wowie[n][j]:
                        temp=[]
                        for y in range(0,len(wowie[0])-j):
                            temp.append(wowie[n][j+y])
                        if a == temp:
                            wowa.append((i,[n,j],"derecha"))
                        temp=[]
                        for y in range(0,len(wowie)-n):
                            temp.append(wowie[n+y][j])
                        if a == temp:
                            wowa.append((i,[n,j],"abajo"))
                        temp=[]
                        if (len(wowie)-n)>=(len(wowie[0])-j):
                            for y in range(0,len(wowie[0])-j):
                                temp.append(wowie[n+y][j+y])
                        else:
                            for y in range(0,len(wowie)-n):
                                temp.append(wowie[n+y][j+y])
                        if a == temp:
                            wowa.append((i,[n,j],"diagonal"))     
    arc.close()
    return wowa
    
if __name__=="__main__":
    pass

           