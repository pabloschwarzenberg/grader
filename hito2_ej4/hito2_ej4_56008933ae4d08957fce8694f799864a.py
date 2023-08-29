p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
lista=[]
def compra(producto,cantidad):
    if producto==p1[0]:
        monto1=p1[2]*cantidad
        lista.appende(monto1)
    if producto==p2[0]:
        monto2=p2[2]*cantidad
        lista.append(monto2)
    if producto==p3[0]:
        monto3=p3[2]*cantidad
        lista.append(monto3)
    if producto==p4[0]:
        monto4=p4[2]*cantidad
        lista.append(monto4)
    if producto==p5[0]:
        monto5=p5[2]*cantidad
        lista.append(monto5)
def ver_producto():
    input("Ingerese ´ver´ si desea ver los prodcutor: ")
    if ver_producto=="ver":
         print("1: Pokemon X")
         print("2: Nintendo XL")
         print("3: Mario Kart 7")
         print("4: PlayStation 4")
         print("5: FIFA 16")

def ver_checkout():
    input("Si desea ver el monto ingrese ´checkout´: ")
    if ver_checkout=="checkout":
         if p1[0]in lista and p2[0]in lista and p3[0] in lista and p4[0]in lista and p5[0]in lista:
              CO= 7*(sum(lista))/20
              print("El checkout es:",CO)
         elif p1[0]in lista and p2[0]in lista and p3[0] in lista:
             CO= (sum(lista))/5
             print("El checkout es:",CO)
         elif p4[0]in lista and p5[0]in lista:
             CO= 3*(sum(lista))/20
             print("El checkout es:",CO)
         else:
             CO= sum(lista)
             print("El checkout es:",CO)
ver_producto()
compra(producto,cantidad)
ver_checkout()
      