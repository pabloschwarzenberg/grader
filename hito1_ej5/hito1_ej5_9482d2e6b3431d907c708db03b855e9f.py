#Cálculo del dígito verificador de un rut
lst = []
sigue = True
while True:
 def string_int(my_data):
     for i in my_data:
         lst.append(int(i))

 rut = input("Enter a number: ")
 string_int(rut)
 if len(lst) == 8:
     num1 = lst[7] * 2
     num2 = lst[6] * 3
     num3 = lst[5] * 4
     num4 = lst[4] * 5
     num5 = lst[3] * 6
     num6 = lst[2] * 7
     num7 = lst[1] * 2
     num8 = lst[0] * 3
     total = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8
     div1 = total / 11
     div2 = total - (11*int(div1))
     resto = 11 - div2
     if resto >= 11:
         print('dv=0')
         break
     elif resto == 10:
         print('dv=k')
         break
     else:
         print('dv=',resto)
         break
 elif len(lst) == 7:
     num1 = lst[6] * 2
     num2 = lst[5] * 3
     num3 = lst[4] * 4
     num4 = lst[3] * 5
     num5 = lst[2] * 6
     num6 = lst[1] * 7
     num7 = lst[0] * 2
     total = num1 + num2 + num3 + num4 + num5 + num6 + num7 
     div1 = total / 11
     div2 = total - (11*int(div1))
     resto = 11 - div2
     if resto >= 11:
         print('dv=0')
         break
     elif resto == 10:
         print('dv=k')
         break
     else:
         print('dv=',resto)
         break
 elif len(lst) == 6:
     num1 = lst[5] * 2
     num2 = lst[4] * 3
     num3 = lst[3] * 4
     num4 = lst[2] * 5
     num5 = lst[1] * 6
     num6 = lst[0] * 7
     total = num1 + num2 + num3 + num4 + num5 + num6  
     div1 = total / 11
     div2 = total - (11*int(div1))
     resto = 11 - div2
     if resto >= 11:
         print('dv=0')
         break
     elif resto == 10:
         print('dv=k')
         break
     else:
         print('dv=',resto)
         break
 else: 
        ('rut ingresado no existe')
        break   