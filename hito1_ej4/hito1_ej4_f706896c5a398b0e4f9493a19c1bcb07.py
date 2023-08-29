#Conversión de Decimal a Binario
tal=int(input("Ingrese numero: "))
t=100
b=""
c=0
while t>=0 :
    if t==0 and tal==0:
        b=b+str(0)
    if (tal-(2**t))>=0 :
        tal=tal-(2**t)
        b=b+str(1)
        c+=1
    elif (tal-(2**t))<0 and c>0 and t!=0:
        b=b+str(0)
    t=t-1        
        
print("resultado=",b)     

