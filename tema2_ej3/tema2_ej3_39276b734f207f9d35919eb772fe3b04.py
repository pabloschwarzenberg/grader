def numero_perfecto(n):
    sum = 0
    i=1
    while i!=n:
        if n%i==0:
            sum=sum+i
        i+=1
    if sum==n:
        return True
    else:
        return False
        
#if _name_ == "_main_":

    n = input("ingrese un número: ")
    if numero_perfecto(n):
        print("El número ingresado" +str(n)+"es perfecto")
    else:
        print("El número ingresado" +str(n)+"no es perfecto")