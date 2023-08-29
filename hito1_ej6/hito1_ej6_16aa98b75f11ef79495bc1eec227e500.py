#ordenar numeros
primero = int(input("ingrese valor 1 : "))
segundo = int(input("ingrese valor 2 : "))
tercero = int(input("ingrese valor 3 : "))               

if primero > segundo:
    if segundo > tercero:
       print("orden de menor a mayor es : ", tercero ,",",segundo,"," ,primero)
    else:
        if primero > tercero:
            print("orden de menor a mayor es : ", segundo ,",",tercero,"," ,primero)
        else:
            print("orden de menor a mayor es : ", segundo ,",",primero,"," ,tercero)
else:
 if segundo > tercero:
     if primero > tercero:
         print("orden de menor a mayor es : ", tercero ,",",primero,"," ,segundo) 
     else:
         print("orden de menor a mayor es : ", primero ,",",tercero,"," ,segundo) 
 
 else:
      print("orden de menor a mayor es : ", primero ,",",segundo,"," ,tercero)
