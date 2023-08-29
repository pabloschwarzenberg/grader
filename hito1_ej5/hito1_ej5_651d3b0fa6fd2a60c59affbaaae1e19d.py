u=str(input())
j=u[::-1]
sl=0
b=0
k=2
for i in j:
    a=int(i)
    l=a*k
    k=k+1
    if k==8:
        k=k-6
    sl=l+sl

s=sl//11
h=11-(sl-s*11)
if h==11:
    print("dv=0")
if h==10:
    print("dv=k")
if h<10:
    print("dv={0}".format(h))