p1=[1,"Pokemon X",33.77]
p1= p1[2]
p2=[2,"Nintendo XL",203]
p2=p2[2]
p3=[3,"Mario Kart 7",27.58]
p3=p3[2]
p4=[4,"PlayStation 4",348.00]
p4=p4[2]
p5=[5,"FIFA 16",51.19]
p5=p5[2]
n1=""; n2=""; n3=""; n4=""; n5=""; n6=""
x1 = input()
x2 = input()
x3 = input()
x4 = input()
x1 = x1.replace(",", ".").split()
x2 = x2.replace(",", ".").split()
x3 = x3.replace(",", ".").split()
x4 = x4.replace(",", ".").split()
maxx= 4

def decimal(x):
    while x > 1:
        x = x - 1
        x = round(x,1)
    return x

def entero(num):
    num = num*10
    return num

def escoger(y):
    if y == 1:
        return p1
    elif y == 2:
        return p2
    elif y == 3:
        return p3
    elif y == 4:
        return p4
    elif y == 5:
        return p5
    
if maxx==4:
    n1= x1[0]
    n2= x2[0]
    n3= x3[0]
    n4= x4[0]
    n1 =float(n1)
    nn1 = decimal(n1)
    n1 = int(n1)
    n2 =float(n2)
    nn2 = decimal(n2)
    n2 = int(n2)
    n3 =float(n3)
    nn3 = decimal(n3)
    n3 = int(n3)
    print(n1, n2, n3)
    if n4 == "checkout":
        if (n1==3 or n1==2 or n1==1) and (n2==3 or n2==2 or n2==1) and (n3==3 or n3==2 or n3==1):
            total = escoger(n1)*entero(nn1)+escoger(n2)*entero(nn2)+escoger(n3)*entero(nn3)
            total = round(total,1)
            total = round(total*0.8, 1)
            print(total)
        elif((n1==4 or n1==5) and (n2==4 or n2==5)) or ((n1==4 or n1==5) and (n3==4 or n3==5)) or ((n2==4 or n2==5) and(n3==4 or n3==5)):
            total = escoger(n1)*entero(nn1)+escoger(n2)*entero(nn2)+escoger(n3)*entero(nn3)
            total = round(total,1)
            total = round(total*0.85, 1)
            print(total)
        
        else:
            print(escoger(n1), entero(nn1),escoger(n2),entero(nn2),escoger(n3),entero(nn3))
            total = escoger(n1)*entero(nn1)+escoger(n2)*entero(nn2)+escoger(n3)*entero(nn3)
            total = round(total,1)
            print(total)
      