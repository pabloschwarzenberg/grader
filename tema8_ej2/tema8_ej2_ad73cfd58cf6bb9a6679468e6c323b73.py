def buscarTodas(a,b):
    i=0
    pos=''
    j=0
    for x in a:
        if j==(a.count(b)-1) and x==b:
            pos=pos+str(i)
            i=i+1
            break
        
        if x==b :
            pos= pos +str(i)+' '
            j=j+1
        i=i+1
    return pos
           