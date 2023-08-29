#Descomponer un número
numero=int(input("Ingrese un número de hasta 4 dígitos:"))

contador=1
control=10

while control<=numero:
    contador+=1
    control*=10


if contador==3:
  centena=(numero//100)
  decena=((numero-centena*100)//10)
  unidad=(numero-(centena*100+decena*10))
  print(centena,"C+",decena,"D+",unidad,"U",sep='')
  
if contador==4:
  umil=numero//1000
  centena=((numero-umil*1000)//100)
  decena=((numero-(centena*100+umil*1000))//10)
  unidad=(numero-(centena*100+decena*10+umil*1000))
  print(umil,"M+",centena,"C+",decena,"D+",unidad,"U",sep='')

if contador==2:
    decena=(numero//10)
    unidad=(numero-decena*10)
    print(decena,"D+",unidad,"U",sep='')

if contador==1:
    unidad=(numero)
    print(unidad,"U",sep='')  