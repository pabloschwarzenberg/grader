n = int(input("Ingrese un número para su descomposición en números primos: "))
print("La descomposición en número primos (considerando los primeros 10) es: ", end="")

i=0
while (i==0) and n>0:
    d2 = n//2
    if (n%2==0):
        print(2,end=" ")
        n = d2
    else:
        i = 1
while (i==1) and n>0:
    d3 = n//3
    if (n%3==0):
        print(3,end=" ")
        n = d3
    else:
        i = 2
while (i==2) and n>0:
    d5 = n//5
    if (n%5==0):
        print(5,end=" ")
        n = d5
    else:
        i = 3
while (i==3) and n>0:
    d7 = n//7
    if (n%7==0):
        print(7,end=" ")
        n = d7
    else:
        i = 4
while (i==4) and n>0:
    d11 = n//11
    if (n%11==0):
        print(11,end=" ")
        n = d11
    else:
        i = 5
while (i==5) and n>0:
    d13 = n//13
    if (n%13==0):
        print(13,end=" ")
        n = d13
    else:
        i = 6
while (i==6) and n>0:
    d17 = n//17
    if (n%17==0):
        print(17,end=" ")
        n = d17
    else:
        i = 7
while (i==7) and n>0:
    d19 = n//19
    if (n%19==0):
        print(19,end=" ")
        n = d19
    else:
        i = 8
while (i==8) and n>0:
    d23 = n//23
    if (n%23==0):
        print(23,end=" ")
        n = d23
    else:
        i = 9
while (i==9) and n>0:
    d29 = n//29
    if (n%29==0):
        print(29,end=" ")
        n = d29
    else:
        i = 10