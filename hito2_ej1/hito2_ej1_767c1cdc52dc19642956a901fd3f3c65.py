a=input()
b=input()
for i in range(0,len(b)):
    if b[i]!=a[i]:
        b=b.replace(b[i],"_"+b[i])
h=len(a)-len(b)
print(b+"_"*h)