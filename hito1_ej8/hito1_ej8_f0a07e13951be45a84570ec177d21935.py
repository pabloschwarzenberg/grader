#Descomponer un número
numero=eval(input("ingrese numero de hasta 4 cifras"))
unidad=numero%10
decena=(numero%100)//10
centena=(numero%1000)//100
mil=(numero//1000)

str_mil = str(mil) + "M"
str_centena=str(centena)+"C"
str_decena=str(decena)+"D"
str_unidad=str(unidad)+"U"




if numero <= 9999:
  print(str_mil,str_centena,str_decena,str_unidad,sep="+")
