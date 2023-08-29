#Descomponer un número
a=int(input("Número de 4 digitos"))
if 0<=a<=9:
   print(a,"U")
elif 10<=a<=99:
   d2=int(a/10)
   u2=int(a-d2*10)
   print(d2,"D +",u2,"U")
elif 100<=a<=999:
   c3=int(a/100)
   d3=int((a-c3*100)/10)
   u3=int(a-c3*100-d3*10)
   print(c3,"C +",d3,"D +",u3,"U")
elif 1000<=a<=9999:
   m4=int(a/1000)
   c4=int((a-m4*1000)/100)
   d4=int((a-m4*1000-c4*100)/10)
   u4=int(a-m4*1000-c4*100-d4*10)
   print(m4,"M +",c4,"C +",d4,"D +",u4,"U")
else:
   print("numero erroneo")

