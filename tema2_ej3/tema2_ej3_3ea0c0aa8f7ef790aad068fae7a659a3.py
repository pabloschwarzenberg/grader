def numero_perfecto(a):
    for i in range (1,1-a):
        if (a%i == 0):
            suma=+i     
            if  (a=6) or (a=28) :
                return True
            elif (a =8):  
                return False  
    
if __name__=="__main__":    
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
