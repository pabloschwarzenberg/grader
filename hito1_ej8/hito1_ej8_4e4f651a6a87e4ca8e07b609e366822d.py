#Descomponer un número
a=input("Número :")
if (len(a)==4):
    b=a[-1]
    c=a[-2]
    d=a[-3]
    e=a[-4]
    print(e,"M","+",d,"C","+",c,"D","+",b,"U")
elif (len(a)==3):
        b = a[-1]
        c = a[-2]
        d = a[-3]
        print( d,"C","+",c,"D","+",b,"U")
elif (len(a)==2):
    b = a[-1]
    c = a[-2]
    print(c,"D","+",b,"U")
elif (len(a)==1):
    b = a[-1]
    print(b,"U")
