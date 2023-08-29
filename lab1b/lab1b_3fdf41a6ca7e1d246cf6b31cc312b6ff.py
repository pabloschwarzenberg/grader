#Heladas
t1=int(input("ingrese la temperatura del sensor n1"))
t2=int(input("ingrese la temperatura del sensor n2"))
t3=int(input("ingrese la temperatura del sensor n3"))


def prendertodos(t1,t2,t3):
    if  t1<=0 or t2<=0 or t3<=0 :
      print("encendido")
      print("encendido")
      print("encendido")
    else:
        def prenderindividual(t1,t2,t3):
            
            if t1<=5 :
                print("encendido")
            else:
                print("apagado")
            if t2<=5:
                print("encendido")
            else:
                print("apagado")
            if t3<=5:
                print("encendido")
            else:
                print("apagado")
        prenderindividual(t1,t2,t3)
        
      
prendertodos(t1,t2,t3)
    