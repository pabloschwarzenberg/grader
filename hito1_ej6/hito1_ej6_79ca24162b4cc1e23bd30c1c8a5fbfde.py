#Ordenar tres números
a=int(input())
b=int(input())
c=int(input())
if(a>=b and a>c and b>=c):
  print("{0},{1},{2}".format(c,b,a))
if(b>=a and b>c and c>=a):
   print("{0},{1},{2}".format(a,c,b))
if(b>=a and b>c and a>=c):
    print("{0},{1},{2}".format(c,a,b))
if(a>=b and a>c and c>=b):
    print("{0},{1},{2}".format(b,c,a))
if(c>=a and c>b and b>=a):
    print("{0},{1},{2}".format(a,b,c))
if(c>=a and c>b and a>=b):
    print("{0},{1},{2}".format(b,a,c))