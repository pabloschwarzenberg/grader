#Descomponer un número
numero=int(input())
num=str(numero)
if len(num)==4:
  unidad=str(numero%10)
  decena=num[2]
  centena=num[1]
  udemil=num[0]
  print(udemil,"M","+",centena,"C","+",decena,"D","+",unidad,"U")
elif len(num)==3:
  unidad=str(numero%10)
  decena=num[1]
  centena=num[0]
  print(centena,"C","+",decena,"D","+",unidad,"U")
elif len(num)==2:
  unidad=str(numero%10)
  decena=num[0]
  print(decena+"D","+",unidad+"U")
elif len(num)==1:
  unidad=str(numero%10)
  print(unidad+"U")



  