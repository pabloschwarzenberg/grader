
#Subsecuencias de ADN
secuencia=input('Ingrese la secuencia: ')
n=int(input('Íngrese el entero: '))
rep=False
list1=[]
list2=[]
for i in range(0,len(secuencia)-n+1):
    a=(secuencia[i:i+n])
    rep=False
    for b in range(0,len(secuencia)-n+1):
        be=secuencia[b:b+n]
        if a==be and (i!=b):
                rep=True
    if not rep:
        print(a)
        list1.append(a)
if list1==list2:
    print('ninguna')