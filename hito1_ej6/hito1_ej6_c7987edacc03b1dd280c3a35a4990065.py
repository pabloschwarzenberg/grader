n1=int(input("ingrese primer numero: "))
n2=int(input("ingrese segundo numero: "))
n3=int(input("ingrese tercer numero: "))
sumatoria=(n1+n2+n3)
nMA=max(n1,n2,n3)
nME=min(n1,n2,n3)
nM=((sumatoria)-(nME)-(nMA))
resultado=(nME,nM,nMA)
print(resultado)