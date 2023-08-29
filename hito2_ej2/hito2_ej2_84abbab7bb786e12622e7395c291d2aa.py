texto=input('ingrese genoma')
texto=list(texto)
a=False
for i in range(0,len(texto)):
    if texto[i]!='a' and texto[i]!='A' and texto[i]!='c' and texto[i]!='C' and texto[i]!='g' and texto[i]!='G' and texto[i]!='t' and texto[i]!='T':
        a=True
if not a:
    print('secuencia correcta')
else:
    print('secuencia incorrecta')
    
