# MCM hito4
# mcm(a,b)= a*b/mcd(a,b)

def mcd(a,b):
    c=1
    lista=[]
    while True:       
        if str(a/c) == str(int(a/c))+".0" and str(b/c) == str(int(b/c))+".0":
            lista.append(c)
        
        if c > a or c > b:
            break
        
        c+=1
    return lista[-1]


def mcm(a,b,ab):
    return(a*b)/mcd(a,b)




if __name__=="__main__":
    pass