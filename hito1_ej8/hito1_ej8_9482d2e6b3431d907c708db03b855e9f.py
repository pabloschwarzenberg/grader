#Descomponer un número
lst = []
sigue = True
while True:
 def string_int(my_data):
     for i in my_data:
         lst.append(int(i))

 num = input("ingrese un numero: ")
 string_int(num)
 
 if len(lst) > 4:
         print('numero ingresado erroneo')
         break
 elif len(lst) == 4:
         print(lst[0],'M + ', lst[1], 'C + ', lst[2],'D + ', lst[3], 'U' )
         break
 elif len(lst) == 3:
         print(lst[0],'C + ', lst[1], 'D + ', lst[2],'U')
         break
 elif len(lst) == 2:
         print(lst[0],'D + ', lst[1], 'U')
         break
 elif len(lst) == 1:
         print(lst[0],'U')
         break
 else:
    break      