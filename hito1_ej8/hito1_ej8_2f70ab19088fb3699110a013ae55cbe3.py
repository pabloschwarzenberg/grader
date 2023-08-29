
n=int(input('ingresa un numero hasta 4 digitos:'))
respaldo=n

d1=n%10
n=n//10
d2=n%10
n=n//10
d3=n%10
n=n//10
d4=n%10
if 0 <= respaldo < 10:
    respuesta=str(d1)+ 'U'
    print(respuesta)
elif 10 <= respaldo < 100:
    respuesta=str(d2)+'D + '+ str(d1)+ 'U'
    print(respuesta)
elif 100 <= respaldo < 1000:
    respuesta=str(d3)+'C + '+ str(d2)+'D + '+ str(d1)+ 'U'
    print(respuesta)
elif 1000 <= respaldo < 10000:
    respuesta=str(d4)+'M + '+ str(d3)+'C + '+ str(d2)+'D + '+ str(d1)+ 'U'
    print(respuesta)