#Descomponer un número
numero=int(input("insertar numero natural de 1,2,3 o 4 cifras"))
if 0<numero<10000:
  m= numero//1000
  c= (numero%1000)//100
  d= ((numero%1000)%100)//10
  u= ((numero%1000)%100)%10
  print(m,"M +",c,"C +",d,"D +",u,"U")