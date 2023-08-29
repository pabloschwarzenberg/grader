x=int(input("ingrese numero:"))

primos=[]
for i in range(2,x+1):
    while ((x%i)==0):
        primos.append(i)
        x=x/i
            

                              
for i in range(len(primos)):
    print(primos[i])