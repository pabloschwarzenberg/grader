#Factores Primos
def primo(n):
d=2
primo=True
while d<n:
    if d%n==0:
     primo=False
     break
    d=d+1
if primo and n>1:
 return("si")
else:
 return("no")
x=int(input())
for i in range(1,x):
  if(primo(i)=='si'):
    g=x//i
    if(primo(g)=='si' and g*i==x)
      print(i)
      print(g)