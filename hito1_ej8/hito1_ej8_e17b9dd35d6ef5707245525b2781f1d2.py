#Descomponer un número
a = int(input("Escriba un numero:"))
a = str(a)
n = len(a)

if (n == 4):

    m = a[0:1]
    c = a[1:2]
    d = a[2:3]
    u = a[3:4]

    print(m,"M +",c,"C+",d,"D+",u,"U")

elif(n == 3):                                                           

     c = a[0:1]
     d = a[1:2]
     u = a[2:3]

     print(c,"C+",d,"D+",u,"U")
     
elif(n == 2):
    a = str(a)
    d = a[0:1]
    u = a[1:2]

    print(d,"D+",u,"U")

elif(n == 1):

    a = str(a)
    u = a[0:1]
    print(u,"U")