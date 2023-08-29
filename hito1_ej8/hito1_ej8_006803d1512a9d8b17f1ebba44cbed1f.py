#Descomponer un número
a=int(input("Escriba un numero de cuatro digitos"))
umillon=a//1000
centena=a-umillon*1000
centena1=centena//100
decena=a-umillon*1000
decena1=centena1*100
decena2=(decena-decena1)//10
unidad=a-umillon*1000
unidad1=centena1*100
unidad2=decena2*10
unidad3=(unidad-unidad1-unidad2)//1
print(umillon,"M+",centena1,"C+",decena2,"D+",unidad3,"U")
