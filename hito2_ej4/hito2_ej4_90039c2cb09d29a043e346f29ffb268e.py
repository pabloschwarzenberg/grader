p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

carro=0
def agregar_al_carro(producto,cantidad):
  if producto==p1:
    return p1*cantidad
  elif producto==p2:
    return p2*cantidad
  elif producto==p3:
    return p3*cantidad
  elif producto==p4:
    return p4*cantidad
  elif producto==p5:
    return p5*cantidad
  carro=carro+producto
  


def ver():
  return carro
  
    
