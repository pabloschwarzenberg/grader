p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
n=input("Ingrese el string del id producto con su cantidad: ")
calcular(n)
def calcular(string):  #5,2
  global p1
  lista_precios20=[]
  lista_precios15=[]
  lista_id20=[]
  lista_id15=[]
  id_producto=string[0]
  cantidad=string[2]
  if id_producto=="1":
    lista_id20.append(int(cantidad)*p1[2])
  elif id_producto=="2":
    lista_id20.append(int(cantidad)*p2[2])
  elif id_producto=="3":
    lista_id20.append(int(cantidad)*p3[2])
  elif id_producto=="4":
    lista_id15.append(int(cantidad)*p4[2])
  elif id_producto=="5":
    lista_id15.append(int(cantidad)*p3[2])
  for i in range(len(lista_id20)):
    print(
    
  
  
  