def suma_divisores(a):
  c=[]
  b=1
  while a>=b:
    x=a%b
    if x==0 and b!=a:
      c.append(b)
    b=b+1
    #print(c)
  q=sum(c)
  if q==1:
    abc=True
  else:
    abc=False
  qwerty=("({0}, {1})".format(q,abc))
  return qwerty

if __name__ == "__main__":

  a=int(input("Indica tu número: "))
  print(suma_divisores(a))

