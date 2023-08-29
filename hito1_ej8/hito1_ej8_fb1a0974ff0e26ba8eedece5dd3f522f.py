#Descomponer un número
n=input("Numero:")
nn=int(n)
ns=str(n)
ns.split(" ")


if nn<10:
    d1=ns[0]
    print(d1,"U")

elif 10<nn<100:
    d1=ns[0]
    d2=ns[1]
    print(d1,"D +",d2,"U")
    
elif 100<nn<1000:
    d1=ns[0]
    d2=ns[1]
    d3=ns[2]
    print(d1,"C +",d2,"D +",d3,"U")

elif 1000<nn<10000:
    d1=ns[0]
    d2=ns[1]
    d3=ns[2]
    d4=ns[3]
    print(d1,"M +",d2,"C +",d3,"D +",d4,"U") 