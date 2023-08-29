#Descomponer un número
n = int(input())
M = n//1000
C = n//100 - 10*M
D = n//10 - 100*C 
U = (n//1) - 1000*D
if n>1000:
  print(M,'M',C,'C',D,'D',U,'U')
elif 100<=n<1000:
  print(C,'C',D,'D',U,'U')
elif 10<=n<100:
  print(D,'D',U,'U')
elif 0<=n<10:
  print(U,'U')
else:
  print('no c, mentira, si c pero no wa decir')