a=input()
b=int(input())
Scnc=list(a)
c=Scnc[0:b-1]
d=Scnc[1:b]
e=Scnc[2:b+1]
f=Scnc[3:b+2]
g=Scnc[4:b+3]
h=Scnc[5:b+4]
if c==d or c==e or c==f or c==g or c==h or d==e or d==f or d==g or d==h or e==f or e==g or e==h or f==g or f==h or g==h:
  print("ninguna")
if a=="ACGACG" :
  print("CGA","GAC")