#Descomponer un número
n=int(input("ingrese un número: "))
m=(n//1000)
c=((n%1000)//100)
d=((n%100)//10)
u=(n%10)
if m!=0 and c!=0 and d!=0 and u!=0:
    print(n//1000,"M","+",(n%1000)//100,"C","+",(n%100)//10,"D","+",n%10,"U")
elif m==0:
    print((n%1000)//100,"C","+",(n%100)//10,"D","+",n%10,"U")
elif c==0:
    print(n//1000,"M","+",(n%100)//10,"D","+",n%10,"U")
elif d==0:
    print(n//1000,"M","+",(n%1000)//100,"C","+",n%10,"U")
elif u==0:
    print(n//1000,"M","+",(n%1000)//100,"C","+",(n%100)//10,"D")
elif m==0 and c==0:
    print((n%100)//10,"D","+",n%10,"U")
elif c==0 and d==0:
    print(n//1000,"M","+",n%10,"U")
elif d==0 and u==0:
    print(n//1000,"M","+",(n%1000)//100,"C")
elif m==0 and d==0:
    print((n%1000)//100,"C","+",n%10,"U")
elif c==0 and u==0:
    print(n//1000,"M","+",(n%100)//10,"D")
elif m==0 and u==0:
    print((n%1000)//100,"C","+",(n%100)//10,"D")
elif m==0 and c==0 and d==0:
    print(n%10,"U")
elif m==0 and c==0 and u==0:
    print((n%100)//10,"D")
elif m==0 and d==0 and u==0:
    print((n%1000)//100,"C")
elif c==0 and d==0 and u==0:
    print(n//1000,"M")


     