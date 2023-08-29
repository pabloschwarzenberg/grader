def mcm(a,b,ab):
    a=int(a)
    b=int(b)
    if a==1 and b==1:
        return 1
    else:
        primos=[2,3,5,7,11,13,17,19,23]
        i=0
        while i<len(primos):
            if a==1:
                if b%(int(primos[i]))==0:
                    a=1
                    b=b/(int(primos[i]))
                    return primos[i]*mcm(a,b,a*b)
                else:
                    i=i+1
            elif b==1:
                 if a%(int(primos[i]))==0:
                    b=1
                    a=a/(int(primos[i]))
                    return primos[i]*mcm(a,b,a*b)
                 else:
                    i=i+1
        
            elif a%(int(primos[i]))==0 and b%(int(primos[i]))!=0:
                 if a%(int(primos[i]))==0 and b%(int(primos[i]))!=0:
                     a=a/(int(primos[i]))
                     b=b
                     return primos[i]*mcm(a,b,a*b)
                 else:
                     i=i+1  
            elif a%(int(primos[i]))!=0 and b%(int(primos[i]))==0:
                 if a%(int(primos[i]))!=0 and b%(int(primos[i]))==0:
                     a=a
                     b=b/(int(primos[i]))
                     return primos[i]*mcm(a,b,a*b)
                 else:
                     i=i+1          
            elif a!=1 and b!=1:
                 if a%(int(primos[i]))==0 and b%(int(primos[i]))==0:
                     a=a/(int(primos[i]))
                     b=b/(int(primos[i]))
                     return primos[i]*mcm(a,b,a*b)
                 else:
                     i=i+1  
if __name__=="__main__":
    print(mcm(88,44,88*44))
           