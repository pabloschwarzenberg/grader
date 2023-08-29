a=int(input("ingrese algun número: "))

p=[]
for i in range(2,a + 1):
    while ((a%i) == 0):
        p.append(i)
        a = a/i
            

                              
for i in range(len(p)):
    print(p[i])