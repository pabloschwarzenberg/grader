a=int(input("ingresa un numero "))
b=int(input("ingresa otro numero "))
c=int(input("ingresa un ultimo numero "))
if((a<=b) and (a<=c)):
  menor=a;
  if(b<=c):
    medio=b;
    mayor=c;
  else:
    medio=c;
    mayor=b;
elif((b<=a) and (b<c)):
  menor=b;
  if(a<=c):
    medio=a;
    mayor=c;
  else:
    medio=c;
    mayor=a
else:
  menor=c;
  if(a<=b):
    medio=a;
    mayor=b;
  else:
    medio=b;
    mayor=a;
print("{},{},{}".format(menor, medio, mayor))