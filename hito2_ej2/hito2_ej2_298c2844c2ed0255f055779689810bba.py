bases=["A","C","G","T","a","c","g","t"]
genoma=input("ingrese genoma:")
c=0
for x in genoma:
    if x not in bases:
       c+=1
if c==0:
    print('secuencia correcta')
else:
    print('secuencia incorrecta')