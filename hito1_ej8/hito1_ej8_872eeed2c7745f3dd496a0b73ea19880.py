#Descomponer un número
s=input("Inserte número:")

s=float(s)

if (s>=1000 and s<=10000):

    s=str(s)

    a=s[3]
    b=s[2]
    c=s[1]
    d=s[0]
    print(d,"M","+",c,"C","+", b, "D", "+", a, "U")

elif (s>=100 and s<=1000):

    s=str(s)

    a=s[2]
    b=s[1]
    c=s[0]
    
    print(c,"C","+", b, "D", "+", a, "U")

elif (s>=10 and s<=100):

    s=str(s)

    a=s[1]
    b=s[0]
    
    
    print( b, "D", "+", a, "U")


elif (s>=0 and s<=10):

    s=str(s)

    a=s[0]
    
    print(a, "U")
 