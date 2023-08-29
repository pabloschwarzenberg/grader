#Descomponer un número
num = int(input())
a = len(str(num))
c =list(str(num))
if a == 4:
  c[0]= str(c[0])+'M'
  c[1]= str(c[1])+'C'
  c[2]= str(c[2])+'D'
  c[3]= str(c[3])+'U'
elif a == 3:
  c[0]= str(c[0])+'C'
  c[1]= str(c[1])+'D'
  c[2]= str(c[2])+'U'  
elif a == 2:
  c[0]= str(c[0])+'D'
  c[1]= str(c[1])+'U'

else:
  c[0]= str(c[0])+'U'
p =''
for i in range(len(c)):
  if i == len(c)-1:
    p= p +str(c[i])
  else:
    p = p +str(c[i])+'+'

print(p)