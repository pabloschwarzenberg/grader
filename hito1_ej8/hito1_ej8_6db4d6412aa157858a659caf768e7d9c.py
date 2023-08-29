#Descomponer un número
num= (input())
dig=[]
for i in range(len(num)):
  dig.append(num[i])
g=0
if len(num)==4:
  print((dig[g]+'M + '+dig[g+1]+'C + '+dig[g+2]+'D + '+dig[g+3]+'U'),sep='')
elif len(num)==3:
  print((dig[g]+'C + '+dig[g+1]+'D + '+dig[g+2]+'U'),sep='')
elif len(num)==2:
  print((dig[g]+'D + '+dig[g+1]+'U'),sep='')  
elif len(num)==1:
  print((dig[g]+'U'),sep='')     