a=input("Escriba el primer número:")
print(a)
b=input("Ecsriba el segundo número:")
print(b)
c=input("Escriba el tercer número:")
print(c)
if (int(a)<=int(b) and int(b)<=int(c)):
    print (a+","+b+","+c)
else:
    if int(a)<=int(c) and int(c)<=int(b):
        print (a+","+c+","+b)
    else:
        if int(b)<=int(a) and int(a)<=int(c):
            print(b+","+a+","+c)
        else:
            if int(b)<=int(c) and int(c)<=int(a):
                print (b+","+c+","+a)
            else:
                if int(c)<=int(a) and int(a)<=int(b):
                    print (c+","+a+","+b)
                else:
                    print (c+","+b+","+a)
