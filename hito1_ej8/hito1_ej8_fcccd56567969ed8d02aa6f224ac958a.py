#Descomponer un número
      
numero=int(input('Ingresa un numero de hasta 4 digitos: '))

respaldo= numero

u= numero%10
numero=numero//10

d=numero%10
numero=numero//10

c=numero%10
numero=numero//10

m=numero

print('\n')     
if 0<=respaldo<10:
    print(str(u)+'U')

if 10<=respaldo<100:
    print(str(d)+'D + '+ str(u)+ 'U')
    
if 100<=respaldo<1000:
    print(str(c)+ 'C + '+ str(d)+ 'D + '+ str(u), 'U')
    
if 1000<=respaldo<10000:
    print(str(m)+ 'M + '+ str(c)+ 'C + '+ str(d)+ 'D + '+ str(u)+ 'U')
