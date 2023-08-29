def mcd(a, b):
    while b:      
        a, b = b, a % b
        
    return a

def mcm(a, b, ab):
    return a * b // mcd(a, b)
    
if __name__=="__main__":
    pass