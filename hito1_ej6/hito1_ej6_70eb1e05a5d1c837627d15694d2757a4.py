#Ordenar tres números
L=[]
for i in range(3):
    N=input("N->")
    L.append(N)
L.sort()
Nums= ''
for i in range(0,len(L)):
    Nums+=str(L[i])
    if i !=len(L)-1:
       Nums+=','

print(Nums)

      