def suma_divisores (x):
    listaa = [] 

    for i in range( 1,x+1 ): 
        
        if x % i == 0: 
            listaa.append(i)
    listaa.remove(x)
    
    if len(listaa)==1:
        return (len(listaa),True)
    else:
        return(sum(listaa),False)

print(suma_divisores(8))