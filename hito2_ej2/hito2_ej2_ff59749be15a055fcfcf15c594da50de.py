secuencia = str(input('Ingrese una secuencia de ADN: '))  
for letra in secuencia:
        if not letra.lower() in "actg":          
               print('secuencia incorrecta')
print('secuencia correcta')

