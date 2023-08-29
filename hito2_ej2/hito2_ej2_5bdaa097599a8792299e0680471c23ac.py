palabra=input('ingrese string debe contrener como secuencia actg: ')
palabra=palabra.upper()
ciclo=0
estado =True
while ciclo<len(palabra):
    if palabra[ciclo]=="A":
        pass
    elif palabra[ciclo]=="C":
        pass
    elif palabra[ciclo]=="T":
        pass      
    elif palabra[ciclo]=="G":
        pass
    else:
        estado = False
        break
    ciclo=ciclo+1
if estado== True:
    print('Secuencia correcta')
else:
    print('secuencia incorrecta')