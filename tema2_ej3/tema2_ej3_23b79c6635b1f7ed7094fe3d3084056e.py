def numero_perfecto(a):
    sumadivs = 0
    for i in range (a):
        if i+1 > a:
            continue
        
        if i+1 == a:
            continue
        
        if a % (i+1) == 0:
            sumadivs += (i+1)
    
    if sumadivs == a:
        return True
    
    elif sumadivs != a:
       return False


if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           