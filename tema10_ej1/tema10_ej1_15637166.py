def mcm(a,b,ab):
    if a>b:
        mayor=a
    else:
        mayor=b
    while True:
        if mayor%a==0 and mayor%b==0:
           MCM=mayor
           break
        mayor+=1
    return MCM
        
   
   

if __name__=="__main__":
    pass
           