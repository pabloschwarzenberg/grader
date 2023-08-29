n=int(input("largo"))

p=[]
c=[]
a=""
for i in range(n):
    p.append("0")
    c.append("0")
    a+="0"
print(a)

for i in range(len(p)):
    a=""
    p[i]="1"
    for j in p:
        a+=j
    print(a)

for i in range(len(c)-1):
    c[len(c)-i-1]="1"
    a=""
    for j in c:
        a+=j
    print(a)