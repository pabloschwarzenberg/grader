#Descomponer un número
n= int(input("Ingrese numero natural de hasta 4 cifras: "))
if 0<n<10000:
    mile=n//1000
    cen=((n%1000))//100
    dec=((n%1000)%100)//10
    uni=((n%1000)%100)%10
    print(str(mile)+"M + "+str(cen)+"C + "+str(dec)+"D + "+str(uni)+"U + " )