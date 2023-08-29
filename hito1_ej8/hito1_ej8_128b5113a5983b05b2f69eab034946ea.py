#Descomponer un número
n=int(input("ingrese su número(hasta 4 digitos): "))
nm=n%1000
nm2=n-nm%1000
nm3=n-nm%100
nm4=n-nm%10
ndm=(n-nm)//1000
ndc=(nm3-nm2)//100
ndu=(n-nm4)
ndd=((n-nm3)-ndu)//10
if(n>=1000):
    print(ndm,"M","+",ndc,"C","+",ndd,"D","+",ndu,"U")
elif(100<=n<1000):
    print(ndc,"C","+",ndd,"D","+",ndu,"U")
elif(10<=n<100):
    print(ndd,"D","+",ndu,"U")
elif(0<=n<10):
    print(ndu,"U")