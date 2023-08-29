def suma_divisores(a): 
    divisor = [1]
    for i in range (2, a):
        if(a % i == 0):
            divisor.append(i)
    if a > 1:
        for i in range(2, a // 2):
            if(a % i) == 0:
                print(False)
    else:
        print(True)  
    
    return sum(divisor)

if __name__ == "__main__":
    a = int(input("ingrese numero:"))
    suma_divisores(a) 
   