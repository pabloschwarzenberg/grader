a=int(input("ingrese su rut: "))
b=(a%10)
c=(((a%100)-(a%10))/10)
d=(((a%1000)-(a%100))/100)
e=(((a%10000)-(a%1000))/1000)
f=(((a%100000)-(a%10000))/10000)
g=(((a%1000000)-(a%100000))/100000)
h=(((a%10000000)-(a%1000000))/1000000)
i=(((a%100000000)-(a%10000000))/10000000)
if (a<=10000000):
  x=(((b*2)+(c*3)+(d*4)+(e*5)+(f*6)+(g*7)+(h*2))%11)
else:
  x=(((b*2)+(c*3)+(d*4)+(e*5)+(f*6)+(g*7)+(h*2)+(i*3))%11)
y=(11-x)
if (y==10):
  print("dv=k")
if (y==0):
  print("dv=0")
if (y==1):
  print("dv=1")
if (y==3):
  print("dv=3")
if (y==4):
  print("dv=4")
if (y==5):
  print("dv=5")
if (y==6):
  print("dv=6")
if (y==7):
  print("dv=7")
if (y==8):
  print("dv=8")
if (y==9):
  print("dv=9")
else:
  print("dv=0")