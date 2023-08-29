p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
      
def carro(producto,cantidad):
    if producto==p1[0]:
      return p1[2]*cantidad
    if producto==p2[0]:
      return p2[2]*cantidad
    if producto==p3[0]:
      return p3[2]*cantidad
    if producto==p4[0]:
      return p4[2]*cantidad
    if producto==p5[0]:
      return p5[2]*cantidad

def checkout(a,b,c):
    if b==6:
        print(round(a*0.8,1))
    if c==9:
        print(round(a*0.85,1))
    


n=0
a=0
b=0
c=0
while n!="checkout":
    n=input()
    if n!="checkout":
        n1=n.split(",")
        x=carro(int(n1[0]),int(n1[1]))
        a+=x
        if n1[0]=="1" or n1[0]=="2" or n1[0]=="3":
            b+=int(n1[0])
        elif n1[0]=="4" or n1[0]=="5":
            c+=int(n1[0])
    if n=="checkout":
        checkout(a,b,c)