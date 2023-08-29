#Cálculo del dígito verificador de un rut
num=int(input("Ingrese rut sin dv: "))
while not(num>=1000000 and num<=99999999):
    num=int(input("Ingrese rut sin dv: "))

a= str(num)[::-1]
print("Numero dado vuelta: ",a)

uno= int (a[0])*2
dos= int (a[1])*3
tre= int (a[2])*4
cua= int (a[3])*5
cin= int (a[4])*6
sei= int (a[5])*7
sie= int (a[6])*2
if(len(a)==8):
    och= int (a[7])*3
else:
    och=0

suma= uno+dos+tre+cua+cin+sei+sie+och


resto= suma%11


dv= 11-resto

print("dv=",dv)

if(dv==10):
    print("dv=k")

if(dv==11):
    print("dv=0")    