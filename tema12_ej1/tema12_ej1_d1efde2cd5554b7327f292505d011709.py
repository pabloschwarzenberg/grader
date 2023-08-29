def binarios(n,n0="",n1=""):
    n = str(n)
    if len(n1)+1 == int(n):
        n0 = n0+"0"
        n1 = n1+"1"
        print(n0+"\n"+n1)
    else:
        n0 = n0+"1"
        binarios(n,n0,n0)
        n1 = n1+"0"
        binarios(n,n1,n1)

n = int(input(""))
binarios(n) 