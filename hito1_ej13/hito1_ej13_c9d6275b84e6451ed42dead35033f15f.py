num=int(input("ingrese un numero: "))
x=0
primos=[]
for i in range(2,num+1):
    while num%i==0:
        primos.append(i)
        num=num/i
       
while x<len(primos):
    print(primos[x])
    x=x+1
        
print(primos)  