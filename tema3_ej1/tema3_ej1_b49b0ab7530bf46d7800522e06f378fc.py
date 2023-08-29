# completa el código de la función
def suma_divisores(num):
    suma=0
    for i in range(1,num):
        if num%i==0:
            suma+=i
            if num<=1:
                return False
            elif num==2:
                return True
            else:
                for i in range(2,num):
                    if num%i==0:
                        return False
                    return suma and True    
            
                
    
def total(num):
    total=str(suma_divisores(num))+","+str(es_primo(num))
    return total
if __name__=="__main__":
    num=int(input("Ingrese el numero: "))
           