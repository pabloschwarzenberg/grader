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
    n = input("Digite un numero: ")
    if numero_perfecto(n):
        print("El numero digitado" +str(n)+" es Perfecto")
    else:
        print("El numero digitado" +str(n)+"No es Perfecto")
           