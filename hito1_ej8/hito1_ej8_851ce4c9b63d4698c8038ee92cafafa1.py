a = eval(input())

m = a//1000
c = (a//100)%10
d = (a//10)%10
u = (a%10)

if m == 0:
    print(c,"C",'+',d,"D",'+',u,"U")
else:
    if m== 0 and c == 0:
        print(d,"D",'+',u,"U")
    else:
        if m == 0 and c == 0 and d == 0:
            print(u,"U")
        else:
            print(m,'M','+',c,"C",'+',d,"D",'+',u,"U")
