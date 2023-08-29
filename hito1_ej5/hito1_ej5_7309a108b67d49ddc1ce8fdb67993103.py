n = int(input("rut: "))

l = n % 10
n= int(n / 10)
k = n% 10
n= int(n / 10)
j = n % 10
n = int(n / 10)
h = n % 10
n = int(n / 10)
g = n % 10
n= int(n / 10)
f = n% 10
n = int(n / 10)
d = n % 10
n= int(n / 10)
s = n % 10
n= int(n / 10)

print(l,k,j,h,g,f,d,s)

lp=l*2
kp=k*3
jp=j*4
hp=h*5
gp=g*6
fp=f*7
dp=d*2
sp=s*3

pp=lp+kp+jp+hp+gp+fp+dp+sp
op=int(pp/11)

qw=pp-(op*11)
w=11-qw

if(w==11):
  print("dv=",(int(0)))
elif(w==10):
  print("dv=K")
else:
  print("dv=",w)