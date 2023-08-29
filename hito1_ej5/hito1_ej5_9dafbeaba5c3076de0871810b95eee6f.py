#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese su rut :"))
digito1= rut//10000000
digito2= rut//1000000 - (rut//10000000)*10
digito3= rut//100000 - (rut//1000000)*10
digito4= rut//10000 - (rut//100000)*10
digito5= rut//1000 - (rut//10000)*10
digito6= rut//100 - (rut//1000)*10
digito7= rut//10 - (rut//100)*10
digito8= rut//1 - (rut//10)*10

Digito8=digito8*2
Digito7=digito7*3
Digito6=digito6*4
Digito5=digito5*5
Digito4=digito4*6
Digito3=digito3*7
Digito2=digito2*2
Digito1=digito1*3

sumaDeTodos=(Digito8+Digito7+Digito6+Digito5+Digito4+Digito3+Digito2+Digito1)

sumaDeTodos2= sumaDeTodos%11

sumaDeTodos3=11-sumaDeTodos2

if sumaDeTodos3==11:
    print("dv=0 ") 
elif sumaDeTodos3==10:
    print("dv=K")
else: 
 print("dv=" + str(sumaDeTodos3))

