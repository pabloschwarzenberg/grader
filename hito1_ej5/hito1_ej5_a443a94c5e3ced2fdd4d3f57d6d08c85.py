num= int(input("ingrese su rut: "))
digitos= len(str(num))
num=str(num)
count= len(num)
rut_inv= []
while count>0:
  rut_inv += num[count-1] 
  count-= 1
for i in range(len(rut_inv)):
  rut_inv[i] = int(rut_inv[i])
list_mult= [2,3,4,5,6,7,2,3]
producto= [x*y for x,y in zip(rut_inv,list_mult)]
sumatoria= sum(producto)
div= sumatoria%11
rest= 11-div
if rest==11:
  print("dv=0")
elif rest==10:
  print("dv=K")
else:
  print("dv=",rest)