p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
def mostrar(carro):
   largo=len(carro)
   i=0
   cant_1=0
   cant_2=0
   cant_3=0
   cant_4=0
   cant_5=0
   while i<largo:
       compra=carro[i]
       prod=compra[0]
       if prod!="checkout":
           cant=compra[2]
           if prod=="1":
               cant_1=cant_1+ int(cant)
           if prod=="2":
               cant_2=cant_2+ int(cant)
           if prod=="3":
               cant_3=cant_3+ int(cant)
           if prod=="4":
               cant_4=cant_4+ int(cant)
           if prod=="5":
               cant_5=cant_5+ int(cant)
       i=i+1
       
   if cant_1>0:
       print(p1[1] + " Cantidad: " + str(cant_1))
   if cant_2>0:
       print(p2[1] + " Cantidad: " + str(cant_2))
   if cant_3>0:
       print(p3[1] + " Cantidad: " + str(cant_3))
   if cant_4>0:
       print(p4[1] + " Cantidad: " + str(cant_4))
   if cant_5>0:
       print(p5[1] + " Cantidad: " + str(cant_5))

       
p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

compra=str()
carro=[]
accion=str()
while accion!="checkout":
   accion=str(input("ingrese: "))
   if accion!="ver":
       carro.append(accion)
   else:
       mostrar(carro)
   

largo=len(carro)
i=0
cant_1=0
cant_2=0
cant_3=0
cant_4=0
cant_5=0
total=0

while i<largo:
   compra=carro[i]
   prod=compra[0]
   if prod!="checkout":
       cant=compra[2]
       if prod=="1":
           cant_1=cant_1+ int(cant)
           total = total + (p1[2]*int(cant))
       if prod=="2":
           cant_2=cant_2+ int(cant)
           total = total + (p2[2]*int(cant))
       if prod=="3":
           cant_3=cant_3+ int(cant)
           total = total + (p3[2]*int(cant))
       if prod=="4":
           cant_4=cant_4+ int(cant)
           total = total + (p4[2]*int(cant))
       if prod=="5":
           cant_5=cant_5+ int(cant)
           total = total + (p5[2]*int(cant))

   i=i+1
   
#Analizo descuentos
final=total
if cant_1>0 and cant_2>0 and cant_3>0:
   descuento= total*20/100
   final=final-descuento
if cant_4>0 and cant_5>0: 
   descuento= total*15/100
   final=final-descuento
final=round(final,1)
print(final)