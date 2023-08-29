def numero_perfecto(a):
    list = []
    for i in range(1, a):
        
        if(a%i == 0):
          
            list.append(i)
     
    if(sum(list)==a):

        k = True

    elif(a == 1):

        k = True

    else:

        k = False

    return k
        
            

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           