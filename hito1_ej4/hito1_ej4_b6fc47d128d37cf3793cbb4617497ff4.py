numero=int(input("numero:"))
divisor=2
b=[]
while divisor<=numero:
    if int(numero)%divisor==0:
        a=int(0)
    elif int(numero)%divisor==1:
        a=int(1)
        divisor=divisor
    b.insert(0,a)
    
    numero=numero//2
b.insert(0,1)
print("resultado=",b)
     