#Cálculo del dígito verificador de un rut
rut=input("ingrese rut: ")
#12345678
if len(rut) == 8:
   rut = int(rut)
   n8 = rut%10
   n7 = (rut%100)//10
   n6 = (rut%1000)//100
   n5 = (rut%10000)//1000
   n4 =(rut//10000)%10
   n3 = (rut//100000)%10
   n2 = (rut//1000000)%10
   n1 = rut//10000000
   
   r1= n8 * 2
   r2= n7 * 3
   r3= n6 * 4
   r4= n5 * 5
   r5= n4 * 6
   r6= n3 * 7
   r7= n2 * 2
   r8= n1 * 3
   
   suma = r1 + r2 + r3 + r4 + r5 + r6 + r7 + r8
   div_entera = suma//11
   resto_div_entera = suma - (11 * div_entera)
   resultado_final = 11 - resto_div_entera
   
   if resultado_final == 11:  
      print("dv =", 0)
      
   elif resultado_final == 10:  
     print("dv =k")
   
   else:  
     print("dv =", resultado_final)

elif len(rut) == 7:  
   rut = int(rut)
   n7 = rut%10
   n6 = (rut%100)//10
   n5 = (rut%1000)//100
   n4 = (rut%10000)//1000
   n3=(rut//10000)%10
   n2 = (rut//100000)%10
   n1 = (rut//1000000)%10
   
   
   r1= n7 * 2
   r2= n6 * 3
   r3= n5 * 4
   r4= n4 * 5
   r5= n3 * 6
   r6= n2 * 7
   r7= n1 * 2
   
   
   suma = r1 + r2 + r3 + r4 + r5 + r6 + r7
   div_entera = suma//11
   resto_div_entera = suma - (11 * div_entera)
   resultado_final = 11 - resto_div_entera
   
   if resultado_final == 11:    
      print("dv =", 0)
      
   elif resultado_final == 10:    
     print("dv =k")
   
   else:    
     print("dv =", resultado_final)

elif len(rut) == 6:  
   rut = int(rut)
   n6 = rut%10
   n5 = (rut%100)//10
   n4 = (rut%1000)//100
   n3 = (rut%10000)//1000
   n2=(rut//10000)%10
   n1 = (rut//100000)%10
  
   r1= n7 * 2
   r2= n6 * 3
   r3= n5 * 4
   r4= n4 * 5
   r5= n3 * 6
   r6= n2 * 7
  
   suma = r1 + r2 + r3 + r4 + r5 + r6 + r7
   div_entera = suma//11
   resto_div_entera = suma - (11 * div_entera)
   resultado_final = 11 - resto_div_entera
   
   if resultado_final == 11:    
      print("dv =", 0)
      
   elif resultado_final == 10:    
     print("dv =k")
   
   else:    
     print("dv =", resultado_final)
  
  




