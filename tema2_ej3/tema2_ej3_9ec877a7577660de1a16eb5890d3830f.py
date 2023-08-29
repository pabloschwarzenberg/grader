def numero_perfecto(a):
    sumatorio = 0
    for i in range(1,a):
        if a % i == 0:
            sumatorio += i
            
    return sumatorio == a

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           
    


    

           