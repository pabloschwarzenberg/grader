n=int(input())
binario=""

while n//2!=0:
    binario=str(n%2) + binario
    n=n//2
if n%2==0:
    binario1=str(0) + binario
    print("resultado=",binario1)
else:
    binario1=str(1) + binario
    print("resultado=",binario1)
