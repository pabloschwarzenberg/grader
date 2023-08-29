a=int(input("Ingrese primer número: "))
b=int(input("Ingrese segundo número: "))
c=int(input("Ingrese tercer número: "))
           
if a<b<c:
          print("Orden de menor a mayor:{},{},{}".format(a,b,c))
elif a<c<b:
         print("Orden de menor a mayor:{},{},{}".format(a,c,b))
elif c<a<b:
         print("Orden de menor a mayor:{},{},{}".format(c,a,b))
elif c<b<a:
          print("Orden de menor a mayor:{},{},{}".format(c,b,a))
elif b<a<c:
          print("Orden de menor a mayor:{},{},{}".fromat(b,a,c))
elif b<c<a:
         print("Orden de menor a mayor:{},{},{}".format(b,c,a))
elif a==b<c:
          print("Orden de menor a mayor:{},{},{}".format(a,b,c))
elif a==c<b:
          print("Orden de menor a mayor:{},{},{}".format(a,c,b))
elif b==c<a:
          print("Orden de menor a mayor:{},{},{}".fromat(b,a,c))
elif c<b==a:
          print("Orden de menor a mayor:{},{},{}".format(c,b,a))
elif a<b==c:
          print("Orden de menor a mayor:{},{},{}".format(a,b,c))