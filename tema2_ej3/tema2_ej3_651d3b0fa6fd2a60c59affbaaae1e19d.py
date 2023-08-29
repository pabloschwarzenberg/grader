def numero_perfecto(a):
    i=1
    k=0
    while i<a:
      if a%i==0:
        k=k+i
        i=i+1
      else:
        i=i+1
    if k==a:
      return True
    else:
      return False

if __name__=="__main__":
  a=int(input())
  print(numero_perfecto(a))

           