p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
n=input()
s=0
cont=[]
while n!="checkout":
  if n=="ver":
    print(s)
    n=input()
  else:
    n2=",".split(n)
    if n2[0]=="1":
      s+=33.77*int(n2[1])
      cont.append[n2[0]]
      n=input()
    elif n2[0]=="2":
      s+=203*int(n2[1])
      cont.append[n2[0]]
      n=input()
    elif n2[0]=="3":
      s+=27.58*int(n2[1])
      cont.append[n2[0]]
      n=input()
    elif n2[0]=="4":
      s+=348*int(n2[1])
      cont.append[n2[0]]
      n=input()
    elif n2[0]=="5":
      s+=51.19*int(n2[1])
      cont.append[n2[0]]
      n=input()
print(s.round(1))
  