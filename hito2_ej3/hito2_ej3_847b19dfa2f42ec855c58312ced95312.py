s=str(input())
i=0
suba=" "
while i+2 <len(s):
    s=s.lower()
    subs=(s[i]+s[i+1]+s[i+2])
    i+=1
    if (subs=="aaa"):
        print("ninguna")
        break
    elif s.count(subs)==1:
        print(subs)
    elif s.count(subs) !=1:
        print("ninguna")

    