x=int(input())
y=""
while x>1:
    a=x%2
    y=str(a)+y
    x=x//2
if x==1:
    y="1"+y
else:
    y="0"+y
y=int(y)
print("resultado=",y)  