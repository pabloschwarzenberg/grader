a=int(input(": "))

b=(a%10)
c=int(a/10)

d=(a%100)
e=int(d/10)
f=int(a/100)

g=(a%1000)
h=int(g/100)
i=int(a/1000)

 
if 0 <= a <= 9:
    print(a,"U")

elif 10 <= a <= 99:
    print(c,"D","+",b,"U")

elif 100 <= a <= 999:
    print(f,"C","+",e,"D","+",b,"U")

elif 1000 <= a <= 9999:
    print(i,"M","+",h,"C","+",e,"D","+",b,"U")
