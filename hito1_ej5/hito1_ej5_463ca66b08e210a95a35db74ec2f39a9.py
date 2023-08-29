rut=str(int(input('ingrese rut')))
formula= '32765432'
i=1
suma=0
for x in str(rut):
    suma= suma + int(rut[-i]) * int(formula[-i])
    i+=1
dv= 11-int(suma%11)
if dv==11:
    dv=0
elif dv==10:
    dv='k'
print ('dv=',dv)
