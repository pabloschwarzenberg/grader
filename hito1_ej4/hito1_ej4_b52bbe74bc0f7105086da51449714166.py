decimal=int(input())
l=[]
while int(decimal)>=1:
    r=int(decimal)%2
    decimal=int(decimal)/2
    l.append(int(r))
    print(int(decimal),",",r)
    
l=l[::-1]
binario=""
for i in l:
    binario+=str(i)
print("resultado="+binario)
