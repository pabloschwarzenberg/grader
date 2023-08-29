#Cálculo del dígito verificador de un rut

#ENTRADA
rut_sin_dv = input("ingrese el rut sin digito verificador: ")

#PROCESO
#iterador que cuenta los digitos del rut
i = 0
#digito que ira multiplicando los digitos del rut (varia del 2 al 7)
mult = 2
#serivira para sumar las multiplicaciones
suma =0
#mientras i no sobrepase los digitos
while(i<len(rut_sin_dv)):
      #
      suma += (int(rut_sin_dv[len(rut_sin_dv)-(1+i)]) * mult)
      mult +=1
      #si mult llega a 8 toma el valor de 2 ya que va desde 2 a 7
      if (mult == 8):
          mult = 2
      i+=1

dv = 11 - (suma % 11)
if(dv==11):
    dv=0
elif(dv==10):
    dv="K"

print("dv =", dv)
