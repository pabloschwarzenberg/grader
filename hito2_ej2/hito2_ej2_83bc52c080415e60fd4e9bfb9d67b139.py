S=input('ingrese secuencia')
S=S.upper()
I=0
estado=True
while I<len(S):
    
    if S[I]=='A':
        pass
    elif S[I]=='C':
        pass
    elif S[I]=='T':
        pass
    elif S[I]=='G':
        pass 
    else:
        estado = False
        break
    I=I+1
if estado==True:
    print ('secuencia correcta')
else:
    print ('secuencia incorrecta') 