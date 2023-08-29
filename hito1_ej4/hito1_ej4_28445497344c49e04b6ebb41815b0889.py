n=int(input())
a=n
b=str()
while a>0:
    b = b + str(a % 2)
    a=a//2
print("resultado=",b[::-1])