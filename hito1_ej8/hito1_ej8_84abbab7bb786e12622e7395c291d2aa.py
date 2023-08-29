#Descomponer
n=input('Ingrese:')
n=int(n)

a=n%100
b=n%1000
c=n%10000
d=n%100000
if n<10:
    print(n,"U")
elif n<100:
    print(n//10,'D+',n%10,"U")
elif n<1000:
        print(n//100,'C+',a//10,'D+',b%10,"U")
    
elif n<10000:
       print(n//1000,'M+',b//100,'C+',((n%1000)%100)//10,"D+",a%10,'U')