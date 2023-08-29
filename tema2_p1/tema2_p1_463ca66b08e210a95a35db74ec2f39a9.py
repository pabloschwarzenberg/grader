#udaudd
i=1
c=0
if __name__ == "__main__":
  n=int(input('Ingrese numero: '))
while i<=n:
  if n/i == int(n/i):
    c+=1
    i+=1
if c==2:
  print('True')
else:
  print('False')