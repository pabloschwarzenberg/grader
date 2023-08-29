def binario(i):
 s=''
 while i>0:
  s = s+ str(i%2)
  i=i/2
  return s[::-1]

 for j in range(1,i+1):
  return binario(j)

if __name__=="__main__":
 n=int(input())
 print(binario(n))