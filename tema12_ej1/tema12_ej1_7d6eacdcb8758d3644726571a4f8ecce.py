n=int(input())

def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario
    
for i in range(0,2**(n)):
  if n == 2:
    for i in range(3):
      print(binarizar(i))   
  elif len(binarizar(i)) == n:
    print(binarizar(i))
           