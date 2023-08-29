#Contestador de celular
n=int(input())
h=int(input())

if 0<=h<=7:
    print("CONTESTAR")
elif h<=14 and n%1000==909:
    print("CONTESTAR")
elif 17<=h<=19 and n//100000!=877:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")