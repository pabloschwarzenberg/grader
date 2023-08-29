def binarios(n,s=""):
        if len(s)==n:
                print (s)
                
        else:
                a=s+"0"
                b=s+"1"
                binarios(n,a)
                binarios(n,b)
                return
        
               


n=int(input())

binarios(n)
           