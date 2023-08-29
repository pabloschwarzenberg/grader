# completa el código de la función
def suma_divisores(a):
    list=[]
    
    for i in range(1,a):
        if(a%i==0):
            list.append(i)

    if(len(list)>2):

        primo = False
    
    elif(a == 1):
    
        primo = False

    else:

        primo = True

    suma = sum(list)

    return(suma,primo)
           