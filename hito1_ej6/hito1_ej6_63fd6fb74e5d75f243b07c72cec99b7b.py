#Ordenar tres números
n1=int(input("ingresa numero uno"))
n2=int(input("ingresa numero dos"))
n3=int(input("ingresa numero tres"))
menor=n1 or n2 or n3
medio=n1 or n2 or n3
mayor=n1 or n2 or n3
if n1<n2 and n3:
      n1==menor
if n2<n1 and n3:
      n2==menor
if n3<n2 and n1:
     n3==menor
if menor==n1 and n2<n3:
      menor=n1
      medio=n2
      mayor=n3
if menor==n2 and n1<n3:
      menor=n1
      medio=n1
      mayor=n3
if menor==n3 and n1<n2:
      menor=n1
      medio=n3
      mayor=n2
if menor==n1 and n3<n2:
       menor=n1
       medio=n3
       mayor=n2
if menor==n2 and n3<n1:
       menor=n2
       medio=n3
       mayor=n1
if menor==n3 and n2<n1:
       menor=n3
       medio=n2
       mayor=n1
print((menor),",",(medio),",",(mayor))