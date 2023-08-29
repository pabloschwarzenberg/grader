def mcm(a,b,ab):
    maximocd=mcd(a,b)
    minimocm=(a*b)/maximocd
    return minimocm
def mcd(a,b):
    resto=a%b
    if resto==0:
        return b
    else:
       dividir=mcd(b,resto)
       return dividir
        
    
    pass

if __name__=="__main__":
    pass
           