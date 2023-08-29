def buscarTodas(a,b):
    i=0
    s=''
    while i<len(a):
        if a[i:i+len(b)]==b:
            s+=str(i)+" "
        i+=1
    return s.strip()
    
if __name__ == "__main__":
    a=input("palabra1: ")
    b=input("palabra2: ")
    c=buscarTodas(a,b)
    print(c)
           