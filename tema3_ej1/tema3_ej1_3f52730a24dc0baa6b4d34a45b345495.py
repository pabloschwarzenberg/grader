def suma_divisores(n):
    suma_div=0
    for i in range(1,n):
        if n%i==0:
            suma_div=suma_div+i
    if suma_div==1:
        return (suma_div,True)
    else:
        return (suma_div,False)
        
if __name__ == "__main__":
    N=int(input("ingresa numero: "))