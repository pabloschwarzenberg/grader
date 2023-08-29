a = int(input())

b = (a % 10) * 2
c = ((a % 100)//10) * 3
d = ((a % 1000)//100) * 4
e = ((a % 10000)//1000) * 5
f = ((a % 100000)//10000) * 6
g = ((a % 1000000)//100000) * 7
h = ((a % 10000000)//1000000) * 2
i = ((a % 100000000)//10000000) * 3

suma = (b+c+d+e+f+g+h+i)
resto = (suma%11)
resta = 11 - resto

if resta == 11:
    print("dv=",0)
else:
    if resta == 10:
        print("dv=","K")
    else:
        print("dv=",resta)
