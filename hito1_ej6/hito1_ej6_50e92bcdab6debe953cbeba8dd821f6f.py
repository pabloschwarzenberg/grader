#Ordenar tres números
x=eval(input('Coloque el número 1:'))
y=eval(input('Coloque el número 2:'))
z=eval(input('Coloque el número 3:'))
 
 
 
 
if x>=y>=z:
    print('El orden sera:',z,',',y,',',x,)
elif x>=z>=y:
    print('El orden sera:',y,',',z,',',x,)
elif y>=z>=x:
    print('El orden sera:',x,',',z,',',y,)
elif y>=x>=z:
    print('El orden sera:',z,',',x,',',y,)
elif z>=x>=y:
    print('El orden sera:',y,',',x,',',z,)
elif z>=y>=x:
    print('El orden sera:',x,',',y,',',z,)
                    
     