#Descomponer un número
num=int(input())
if num/1000 >= 1:
    m=num//1000
    aux1=num%1000
    c=aux1//100
    aux2=num%100
    d=aux2//10
    u=aux2%10
    print(m,"M"," + ",c,"C"," + ",d,"D"," + ",u,"U",sep="")
    
elif num/100 >=1:
    c=num//100
    aux1=num%100
    d=aux1//10
    u=aux1%10
    print(c,"C"," + ",d,"D"," + ",u,"U",sep="")
    
elif num/10 >=1:
    d=num//10
    u=num%10
    print(d,"D"," + ",u,"U",sep="") 
    
else:
    print(num,"U",sep="")