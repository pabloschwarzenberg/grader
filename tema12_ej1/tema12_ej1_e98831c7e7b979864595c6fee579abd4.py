n=int(input())
i=0
def combinacion_binarios(n,i):
    a=bin(i)
    binario=a[2::]
    i+=1
    if len(binario)<=n and len(binario)<10:
      print(binario)
    while len(binario)<=n and len(binario)<10:
      return combinacion_binarios(n,i)
     
combinacion_binarios(n,0)