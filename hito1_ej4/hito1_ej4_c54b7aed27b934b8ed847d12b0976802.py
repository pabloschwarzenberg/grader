#Conversión de Decimal a Binario
num=int(input("inserte un nuero: "))
result=""
r=num
f=r
def paridad(a):
    if (a%2)==0.0:
        return 1
    elif (a%2)!=0.0:
        return 0
while (r//1)>=1:
    f=(f%2)
    if paridad(f)==1.0:
        result=("0"+result)
    elif paridad(f)==0.0:
        result=("1"+result)
    print (f)
    r=int(r/2)
    f=r    
print ("resultado=",result)     
 