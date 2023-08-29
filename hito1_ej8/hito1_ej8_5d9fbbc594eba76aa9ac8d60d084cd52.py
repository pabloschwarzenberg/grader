#Descomponer un número
numero = int(input("Ingrese el numero: "))
m = numero//1000
c = (numero%1000)//100
d = (numero%100)//10
u = (numero%10)

if m>0:
    print(str(m)+"M + "+str(c)+"C + "+str(d)+"D + "+str(u)+"U")
elif m<=0 and c>0:
    print(str(c)+"C + "+str(d)+"D + "+str(u)+"U")
elif m<=0 and c<=0 and d>0:
    print(str(d)+"D + "+str(u)+"U")
elif m<=0 and c<=0 and d<=0:
    print(str(u)+"U")
     