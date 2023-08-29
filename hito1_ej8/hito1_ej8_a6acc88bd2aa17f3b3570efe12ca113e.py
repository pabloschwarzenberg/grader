n=input(":")
l=["M","C","D","U"]
r=""
if len(n)<4:
    for x in range(len(l)-len(n)):
        l.pop(x)
for x in range(len(n)):
    if x!=len(n)-1:
        r+=n[x]+l[x]+" + "
    else:
        r+=n[x]+l[x]
print(r)