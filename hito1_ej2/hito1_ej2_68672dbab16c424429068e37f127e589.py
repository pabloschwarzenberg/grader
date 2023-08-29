numero=int(input())
h=int(input())

if 0<=h<=7:
    print("CONTESTAR")
elif 7<=h<=14 and (numero-909)%1000==0:
    print("CONTESTAR")
elif 17<=h<=19 and not 87700000<=numero<=87799999:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")