def buscarTodas(a,b):
    i=0
    desde=0
    union=""
    #(’tres tristes tigres’,’t’) (0 5 9 13)
    while i<len(a):
        if a.find(b,desde,len(a))==-1:
            break
        union=union+str(a.find(b,desde,len(a)))
        desde=a.find(b,desde)+1
        union = union + " "
        i+=1
    union=union.strip()
    return(union)


if __name__ == "__main__":
    pass
           