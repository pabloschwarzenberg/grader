num = int(input("numero natural de 1,2,3 o 4 cifras:"))
if num>0:
    m = num//1000
    c = (num%1000)//100
    d = ((num%1000)%100)//10
    u = ((num%1000)%100)%10
    print(str(m)+"M+"+str(c)+"C+"+str(d)+"D+"+str(u)+"U")

else:
     print("debe ser un numero de hasta 4 cifras")