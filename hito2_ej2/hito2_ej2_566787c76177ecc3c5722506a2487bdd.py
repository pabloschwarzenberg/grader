palabra=input('ingrese una palabra: ')
palabra=palabra.upper()

I=0
cuenta_letras_incorrectas=0
while I<len(palabra):
    print(palabra[I])
    if palabra[I]!='C' and  palabra[I]!='T' and  palabra[I]!='G' and  palabra[I]!='A':
        cuenta_letras_incorrectas=cuenta_letras_incorrectas+1
    I=I+1
if cuenta_letras_incorrectas==0:
    print('secuencia correcta')
else:
    print('secuencia incorrecta')