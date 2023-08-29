string=input('String: ')
string.upper()
a=0

for i in string:
    if i!='A' and i!='B' and i!='G' and i!='T':
        a=a+1
if a==0:
    print('Secuencia correcta')
if a!=0:
    print('Secuencia incorrecta')
    