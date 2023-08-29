i=int(input())
a=int(input())
h=int(input())
b=int(input())
c=str(input())
w=str(input())

k=0

if b>10:
      if h>=2:
          k=1
if c=="C":
        if h>=3:
            if a<=1973 and a>=1963:
                k=1
if i>=2500000:
        if c=="S":
            if w=="U":
                k=1
if i>=3500000:
        if b>5:
            k=1
if w=="R":
        if c=="C":
            if h<2:
                k=1
 
if k==1:
    print("APROBADO")
if k==0:
    print("RECHAZADO")