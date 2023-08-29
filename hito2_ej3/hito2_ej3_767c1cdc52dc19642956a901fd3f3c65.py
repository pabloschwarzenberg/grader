x=input()
y=int(input())
z=0
listilla=[]
imprimir=0
for i in range(0,len(x)):
    if i+3<=len(x):
        listilla.append(x[i:i+y])
for i in range(0,len(listilla)):
    for j in range(0,len(listilla)):
        if listilla[i]!=listilla[j]:
            z+=1
    if z==len(listilla)-1:
        print(listilla[i])
        imprimir+=1
    z=0
if imprimir==0:
    print("ninguna")
