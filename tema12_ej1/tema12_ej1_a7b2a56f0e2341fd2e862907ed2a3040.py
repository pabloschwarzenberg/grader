def binarios(n,l=[],l2=[]):
    if n<len(l):
       return
    if n==len(l):
        l2.append(l)
    j=['0','1']
    for q in j:
       l.append(q)
       binarios(n,l.copy(),l2)
       l.pop()
    return l2
n=int(input())
for i in binarios(n):
    print ("".join(i))
    
           