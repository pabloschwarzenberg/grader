p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
l=[]
l2=[]
m=["Pokemon X", "Nintendo XL", "Mario Kart 7", "PlayStation 4", "FIFA 16"]
n=[33.77, 203, 27.58, 348.00, 51.19]
while True:
  a=input()
  if a=="checkout":
    break
  elif a=="ver":
    for i in l:
      print(i[0])
  else:
    l.append((int(a[0]),int(a[2])))
    l2.append(int(a[0]))

total=0
for i in l:
  total+=n[i[0]-1]*i[1]
if 1 in l2 and 2 in l2 and 3 in l2:
  total=total*0.8
if 4 in l2 and 5 in l2:
  total=total*0.85
print(total)


    