a=input("").upper()
n=int(input(""))
y=[]
for i in range (len(a)-n):
    x= a[i:i+n]
  
    
    if a.count(x)== 1:
        y.append(x)

for i in y:
    if y.count(i)>1:
        while y.count(i)>0:
           y.remove(i)
if y==[]:
    y.append("ninguna")
print(y)

        