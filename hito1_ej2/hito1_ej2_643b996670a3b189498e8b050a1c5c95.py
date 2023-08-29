#Contestador de celular
n=input()
h=int(input())
a=int(n[0])
b=int(n[1])
c=int(n[2])
g=int(n[5])
e=int(n[6])
f=int(n[7])
if h>=0 and h<=7:
    print("CONTESTAR")
elif h>=7 and h<=14 and g==9 and e==0 and f==9:
    print("CONTESTAR")
elif h>=7 and h<=14 and g!=9 or e!=0 or f!=9:
    print("NO CONTESTAR")
elif h<=14 and h>=19 and a==8 and b==7 and c==7:
    print("NO CONTESTAR")
elif h<=14 and h>=19 and a!=8 or b!=7 or c!=7:
    print("CONTESTAR")
elif h>19 and h<23:
    print("NO CONTESTAR")