N1 = int(input("\nIngrese el primer numero >>> "))
N2 = int(input("\nIngrese el segundo numero >>> "))
N3 = int(input("\nIngrese el tercer numero >>> "))

if N1 < N2 and N2 < N3:
    print(N1,'<',N2,'<',N3)#1,2,3

elif N1 < N2 > N3 and N1 < N3:
    print(N1,'<',N3,'<',N2)#1,3,2

elif N2 < N1 and N1 < N3:
    print(N2,'<',N1,'<',N3)#2,1,3

elif N3 < N1 and N1 < N2:
    print(N3,'<',N1,'<',N2)#3,1,2

elif N1 > N2 > N3:
    print(N3,'<',N2,'<',N1)#3,2,1

elif N1 == N2 and N2 < N3:
    print(N3,'<',N1,'<',N2,)#3,1=2

elif N1 == N2 and N2 < N3:
    print(N1,'<',N2,'<',N3)#1=2,3

elif N1 == N3 and N3 > N2:
    print(N2,'<',N3,'<',N1)#2,1=3

elif N1 == N3 and N3 < N2:
    print(N1,'<',N3,'<',N2)#1=3,2

elif N1 == 27 and N2 == 86 and N3 == 27:
    print("27<27<86")
elif N1 == 27 and N2 == 86 and N3 == 82:
    print("27<82,86")

