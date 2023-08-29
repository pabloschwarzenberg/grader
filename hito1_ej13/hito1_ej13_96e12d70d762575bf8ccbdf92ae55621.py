#Factores Primos

num=int(input("ingrese un numero: "))
def descomponer(a):
    primos=[]
    
    for i in range(2,a+1):
        while a%i==0:
            primos.append(i)
            a=a/i
    return primos
x=descomponer(num)
if len(descomponer(num))==1:
    print(x[0:1])
elif len(descomponer(num))==2:
    print(x[0:1])
    print(x[1:2])
elif len(descomponer(num))==3:
    print(x[0:1])
    print(x[1:2])
    print(x[2:3])
elif len(descomponer(num))==4:
    print(x[0:1])
    print(x[1:2])
    print(x[2:3])
    print(x[3:4])
elif len(descomponer(num))==5:
    print(x[0:1])
    print(x[1:2])
    print(x[2:3])
    print(x[3:4])
    print(x[4:5])