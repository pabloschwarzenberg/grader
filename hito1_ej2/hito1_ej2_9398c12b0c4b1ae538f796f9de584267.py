#Contestador de celular
n=int(input())
h=int(input())
if 8>h:
    print("CONTESTAR")
elif h<14 and h>7:
    if n%1000==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif h>17 and 19>h:
    if n//100000==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")