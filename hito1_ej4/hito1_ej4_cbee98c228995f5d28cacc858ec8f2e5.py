#Conversión de Decimal a Binario
Num_bin=[]

x=int(input('Ingresa tu número decimal\n'))

while x!=0:
    Num_bin.append(x%2)
    x=x//2
Num_bin=Num_bin[::-1]
i=0
a=' '
while i<len(Num_bin):
    a=a+str(Num_bin[i])
    i=i+1
b=int(a.strip(' '))
print('resultado='+str(b))