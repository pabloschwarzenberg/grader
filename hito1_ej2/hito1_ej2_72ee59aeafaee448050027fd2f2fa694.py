#Contestador de celular
n=int(input("ingresa un numero telefonico: "))
h=int(input("ingresa una hora: "))

a=n//10000000
b=n//1000000-(a*10)
c=n//100000-(a*100+b*10)
d=n//10000-(a*1000+b*100+c*10)
e=n//1000-(a*10000+b*1000+c*100+d*10)
f=n//100-(a*100000+b*10000+c*1000+d*100+e*10)
g=n//10-(a*1000000+b*100000+c*10000+d*1000+e*100+f*10)
i=n-(a*10000000+b*1000000+c*100000+d*10000+e*1000+f*100+g*10)

y=a*100+b*10+c
x=f*100+g*10+i

if 0<h<7:
    print("CONTESTAR")
else:
    if h<14:
        if x==909:
          print("CONTESTAR")
        else:
            print("NO CONTESTAR")
    else:
        if 17<h<19:
            if y==877:
                print("NO CONTESTAR")
            else:
                print("CONTESTAR")
        else:
            if h>19:
                print("NO CONTESTAR")