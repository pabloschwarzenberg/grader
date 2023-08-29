def numero_perfecto(a):
    b = a 
    sum = 0 
  
    while b>1: 
        b -= 1 
        if a%b == 0: 
            sum += b 

    if sum == a: 
        return True
    else:  
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))