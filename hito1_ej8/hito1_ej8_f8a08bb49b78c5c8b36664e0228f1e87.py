#Descomponer un número
num = int(input("ingrese un numero de 4 digitos: "))      
if 0< num <10000:
  uni=((num%1000)%100)%10
  dec=((num%1000)%100)//10
  cen=(num%1000)//100
  uni_m=(num//1000)
  print(f"{uni_m}M + {cen}C + {dec}D + {uni}U")
else:
  print("debe ser numero de 4 cifras")