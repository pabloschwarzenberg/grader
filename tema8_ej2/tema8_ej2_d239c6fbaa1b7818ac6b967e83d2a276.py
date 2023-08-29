
def buscarTodas(a,b):
    num=0
    presentar=[]
    a=list(a)
    while num<len(a):
        if a[num]==b:
            presentar.append(str(num))
           
            
        num+=1
    
    return print(*presentar)  
           