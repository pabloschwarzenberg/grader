n=int(input())
binario=str("")
while (n>=1):
    if (n%2 ==0):
        a=0
    else:    
        a=1
    n=n//2
    binario +=str(a)
    inverso= (binario[::-1])
print("resultado="+inverso)
