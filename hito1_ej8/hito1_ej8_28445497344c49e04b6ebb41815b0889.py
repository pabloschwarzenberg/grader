n=str(input())
lista=["U","D","C","M"]
n=n[::-1]
a=len(n)-1
b=str()
while a>=0:
    b=b+n[a]+lista[a]+" + "
    a=a-1
print(b[:-3:1])