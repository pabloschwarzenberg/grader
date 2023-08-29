#Conversión de Decimal a Binario
num=int(input("ingrese su número decimal:"))
lista=[]
while num>0:
    ro=int(num%2)
    lista.append(ro)
    num=(num-ro)/2
n_bin=""
for e in lista [::-1]:
    n_bin=n_bin+str(e)
print("resultado="+str(n_bin))