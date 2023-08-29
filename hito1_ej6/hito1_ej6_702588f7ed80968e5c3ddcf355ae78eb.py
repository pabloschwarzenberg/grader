#Ordenar tres números
x1=int(input("a:" ))
x2=int(input("b:" ))
x3=int(input("c: "))
if (x1>=x2 and x1>=x3 and x2>=x3):
    print(x3,",",x2,",",x1)
elif(x1>=x2 and x1>=x3 and x2<=x3):
    print(x2,",",x3,",",x1)
elif(x1<=x2 and x1>=x3 and x2>=x3):
    print(x3,",",x1,",",x2)   
elif(x1<=x2 and x1<=x3 and x2<=x3):
    print(x1,",",x2,",",x3)
elif(x1<=x2 and x1<=x3 and x2>=x3):
    print(x1,",",x3,",",x2)
elif(x1>=x2 and x1<=x3 and x2<=x3):
    print(x2,",",x1,",",x3)
     