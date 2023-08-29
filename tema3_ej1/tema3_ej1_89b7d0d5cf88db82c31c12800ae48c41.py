def suma_divisores(numero):
     ndos = []
     for x in range(1, numero):
         if (numero % x) == 0:
             ndos.append(x)
     if sum(ndos) == 1:
         return 1, True
     else:
         return sum(ndos), False

     if name == 'main':
       ntres = int(input("ingrese el valor: "))  
       print(suma_divisores(ntres))