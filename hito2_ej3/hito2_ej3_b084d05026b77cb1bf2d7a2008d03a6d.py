s= input()
n= int(input())

def revisar(s, n):
    l=[]
    sub=[]
    r = s.upper()
    for i in range(0, len(r) - n + 1):
        l.append(r[i : i + n])
    string_grande= "".join(l)
    for j in range(0, len(l)):
        if string_grande.count(l[j])==1:
            sub.append(l[j])
    return sub

sub = revisar(s, n)
if len(sub)>=1:
    for t in range(0, len(sub)):
        print(sub[t])
else:
    print("ninguna")