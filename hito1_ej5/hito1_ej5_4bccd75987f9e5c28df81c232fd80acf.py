#Cálculo del dígito verificador de un rut
n = eval (input("Número de 8 digitos:"))
digito1 = (n //10000000 )
digito2= (n//1000000) % 10
digito3= (n//100000) % 10
digito4= (n//10000) % 10
digito5= (n//1000) % 10
digito6= (n//100) % 10
digito7= (n//10) % 10
digito8= n % 10

formula = (digito8*2) + (digito7*3) + (digito6*4) + (digito5*5) + (digito4*6) + (digito3*7) + (digito2*2 ) + (digito1*3)
formula2 = formula // 11
formula3 = formula -(11 * formula2)
dv = 11 - formula3
if dv == 11:
    print("dv = 0")
if dv == 10:
     print("dv = k")
else: 
   print("dv =", dv)