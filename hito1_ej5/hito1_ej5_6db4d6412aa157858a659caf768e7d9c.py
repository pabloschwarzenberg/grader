#Cálculo del dígito verificador de un rut
l=(input('ingrese su rut sin el digito verificador'))
cub=[]
for i in range(len(l)):
    cub.append(int(l[i]))
log=len(l)-1
inver=[]
while True:
    inver.append(int(cub[int(log)]))
    log-=1
    if log==-1:
        break
list1 = (inver)
if len(inver)==8:
    list2 = [2,3,4,5,6,7,2,3]
elif len(inver)==7:
    list2 = [2,3,4,5,6,7,2]
product = [x*y for x,y in zip(list1,list2)]
total=0
for i in range(len(product)):
    total=product[i]+total
digito=11-(total-(int(total/11)*11))
if digito==10:
  digito='k'
  print('dv=',digito)
elif digito==11:
  digito=0
  print('dv=',digito)
else:
  print('dv=',digito)