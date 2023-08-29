def buscarTodas(a,b):
    i=0
    l=""
    while i <len(a):
        if a[i] == b:
            l+=str(i)
            l+=" "
        i+=1
    k=l.rstrip(" ")
    return k
if __name__=="__main__":
    a=input()
    b=input()
    print(buscarTodas(a,b))