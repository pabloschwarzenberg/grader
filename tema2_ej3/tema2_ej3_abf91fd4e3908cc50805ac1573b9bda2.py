def numero_perfecto(a):
    
    h = 0
    
    for x in range(1,a):
        
        if a%x == 0:
            
            h+=x
            
    if h == a:
        
        return True
        
    else: 
        
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           