rut=int(input("Ingrese Rut, sin puntos, guion o DV: \n"))
sum=0
fact=2
while rut>0:
    sum+=((rut%10)*fact)
    rut=rut//10
    fact+=1
    if fact>7:
        fact=2
dv=11-(sum%11)
print(dv)
if dv==11:
   print("dv=0")
elif dv==10:
    print("dv=K")
else:
    print("dv="+str(dv))