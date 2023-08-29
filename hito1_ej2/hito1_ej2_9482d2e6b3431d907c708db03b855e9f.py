#Contestador de celular
lst = []
sigue = True
while True:
 def string_int(my_data):
     for i in my_data:
         lst.append(int(i))

 num = input("Enter a number: ")
 string_int(num)
 total = len(lst)
 if total > 9:
    print('numero ingresado no existe')
    break
 elif total < 8:
    print('numero ingresado no existe')
    break
 else:
    end = lst[5],lst[6],lst[7]
    ini = lst[0],lst[1],lst[2]
    if total == 8:
     hora = int(input('ingrese hora de llamada: '))
     if hora > 23 or hora < 0:
         print('hora ingresada invalida')
         break
     elif hora >= 0 and hora <= 7:
         print('CONTESTAR')
         break
     elif hora >= 8 and hora <= 14:
         if end == (9, 0, 9):
             print('CONTESTAR')
             break
         else:
          print('No CONTESTAR')
          break
     elif hora >= 17 and hora<= 19:
         if ini == (8, 7, 7):
             print ('NO CONTESTAR')
             break
         else:
             print('CONTESTAR')
             break
     else:
         print('NO CONTESTAR')
         break
              