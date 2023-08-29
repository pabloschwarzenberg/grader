#Descomponer un número
n=int(input("Ingrese un numero de hasta 4 cifras: "))
a=n%10
n=n//10
b=n%10
n=n//10
c=n%10
n=n//10
d=n%10
n=n//10
if d>=1:
    print(d,"M+",end=" ")
    if c>=1:
        print(c,"C+",end =" ")
        if b>=1:
            print(b,"D+",end=" ")
            if a>=1:
                print(a,"U")
            if a==0:
                print(a,"U")
        if b==0:
            print(b,"D",end=" ")
    if c==0:
        print(c,"C+",end=" ")
        if b>=1:
            print(b,"D+",end=" ")
            if a>=1:
                print(a,"U")
            if a==0:
                print(a,"U")
        if b==0:
            print(b,"D+",end=" ")
            if a>=1:
                print(a,"U")
            if a==0:
                print(a,"U")
if c>=1:
        print(c,"C+",end =" ")
        if b>=1:
            print(b,"D+",end=" ")
            if a>=1:
                print(a,"U")
            if a==0:
                print(a,"U")
        if b==0:
            print(b,"D+",end=" ")
if b>=1:
            print(b,"D+",end=" ")
            if a>=1:
                print(a,"U")
          
if a>=1:
                print(a,"U")
if a==0:
                print(a,"U")      