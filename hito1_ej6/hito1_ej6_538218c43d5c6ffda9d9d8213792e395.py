#Ordenar tres números
x= int(input('digite un numero entero x: '))
y= int(input('digite un numero entero y: '))
z= int(input('digite un numero entero z: '))

if y==x==z:
    print( '',z , ',' , '',x , ',' , '',y ,',','Todos los numeros ingresados son iguales')  
elif x>=y>=z:
    print( '',z , ',' , '',y , ',' , '',x )
elif x>=z>=y:
    print('' ,y , ',' , '',z , ',' , '',x)
elif y>=x>=z:
    print( '',z , ',' , '',x , ',' , '',y )
elif y>=z>=x:
    print( '',x , ',' , '',z , ',' , '',y )
elif z>=x>=y:
    print( '',y , ',' , '',x , ',' , '',z )
elif z>=y>=x:
    print( '',x , ',' , '',y , ',' , '',z )