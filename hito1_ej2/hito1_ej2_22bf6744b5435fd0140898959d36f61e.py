x=int(input("Ingrese el numero de la llamada: "))
hr=int(input("Ingrese la hora de la llamada: "))

a=x//10000000
b=(x//1000000)-(a*10)
c=(x//100000)-((a*100)+(b*10))
d=(x//10000)-((a*1000)+(b*100)+(c*10))
e=(x//1000)-((a*10000)+(b*1000)+(c*100)+(d*10))
f=(x//100)-((a*100000)+(b*10000)+(c*1000)+(d*100)+(e*10))
g=(x//10)-((a*1000000)+(b*100000)+(c*10000)+(d*1000)+(e*100)+(f*10))
h=x-((a*10000000)+(b*1000000)+(c*100000)+(d*10000)+(e*1000)+(f*100)+(g*10))

y=a*100+b*10+c
z=f*100+g*10+h

if 0<hr<7:
    print("CONTESTAR")

else:
    if h<14:
        if z==909:
            print("CONTESTAR")

        else:
            print("NO CONTESTAR")
        
    else:
        if 17<hr<19:
            if y==877:
                print("NO CONTESTAR")

            else:
                print("CONTESTAR")
            
        else:
            if hr>19:
                print("NO CONTESTAR")
      