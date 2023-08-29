def binario(n,string="",):
    if len(string)==n:
        print(string)
        return
    if n==1:
        for i in range(n):
            for e in range(2):
                binario(n,string+str(e))
    else:
        for i in range(n-(n-1)):
            for e in range(2):
                binario(n,string+str(e))

binario(6,"")
           