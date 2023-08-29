s=input()
s=s.lower()
n=int(input())
ya_salieron=""
totales=[]
i=0
while i<(len(s)-n):
  sub=s[i:i+n]
  if s.find(sub,(i+1))==-1 and ya_salieron.find(sub)==-1:
    print(sub.upper())
    totales.append(sub)
  else:
    ya_salieron=ya_salieron+","+sub
  i=i+1
if totales==[]:
  print("ninguna")