numero_x=float(input("ingrese el factor de la incognita x en la primera ecuación:"))
numero_y=float(input("ingrese el factor de la incognita y en la primera ecuación:"))
numero_c=float(input("ingrese el factor constante en la primera ecución:"))

numero_x2=float(input("ingrese el factor de la incognita x en la segunda ecuación:"))
numero_y2=float(input("ingrese el factor de la incognita y en la segunda ecuación:"))
numero_c2=float(input("ingrese el factor constante en la segunda ecuación:"))

print(numero_x, "x", "+", numero_y, "y", "=", numero_c)
print(numero_x2, "x","+", numero_y2, "y", "=", numero_c2)



if((numero_x!=numero_x2)and(numero_y!=numero_y2)):
    nueva_xarriba=numero_x*numero_x2
    nueva_xabajo=numero_x2*numero_x
    nueva_yarriba=numero_y*numero_x2
    nueva_yabajo=numero_y2*numero_x
    nueva_carriba=numero_c*numero_x2
    nueva_cabajo=numero_c2*numero_x

    suma_y=nueva_yarriba-nueva_yabajo
    suma_c=nueva_carriba-nueva_cabajo
    valor_y=suma_c/suma_y
    

    valor_x=((nueva_carriba)-((nueva_yarriba)*valor_y))/nueva_xarriba
    
    print("x="+str(round(valor_x,1)),"y="+str(round(valor_y,1)))
    


elif (numero_x==numero_x2):
    suma_y=numero_y-numero_y2
    suma_c=numero_c-numero_c2
   
    valor_y=suma_c/suma_y
    valor_x=((numero_c)-((numero_y)*valor_y))/numero_x
    
    print("x="+str(round(valor_x,1)),"y="+str(round(valor_y,1)))

elif (numero_y==numero_y2):
    suma_x=numero_x-numero_x2
    suma_c=numero_c-numero_c2
   
    valor_x=suma_c/suma_x
    valor_y=((numero_c)-((numero_x)*valor_y))/numero_y

    
    print("x="+str(round(valor_x,1)),"y="+str(round(valor_y,1)))