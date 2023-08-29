p1=0
p2=0
p3=0
p4=0
p5=0
valor_de_todo=0
carrosxdd=[]
def carro(stuff):
      global valor_de_todo
      global p1
      global p2
      global p3
      global p4
      global p5
      global carrosxdd
      if stuff=="checkout":
       p=round(valor_de_todo,1)
       return p
      elif int(stuff[0])==1:
          p1=33.77*float(stuff[2])
          carrosxdd.append(str(stuff[0]))
      elif int(stuff[0])==2:
          p2=203*float(stuff[2])
          carrosxdd.append(str(stuff[0]))
      elif int(stuff[0])==3:
          p3=27.58*float(stuff[2])
          carrosxdd.append(str(stuff[0]))
      elif int(stuff[0])==4:
          p4=348.00*float(stuff[2])
          carrosxdd.append(str(stuff[0]))
      elif int(stuff[0])==5:
          p5=51.19*float(stuff[2])
          carrosxdd.append(str(stuff[0]))
      valor_de_todo=p1+p2+p3+p4+p5
      if ('1') in carrosxdd and ("2") in carrosxdd and ("3") in carrosxdd:
           valor_de_todo=(valor_de_todo*80)/100
      elif ('4') in carrosxdd and ("5") in carrosxdd:
           valor_de_todo=(valor_de_todo*85)/100

while True:
  carro(input())
  carro(input())
  carro(input())
  print(carro(input()))
  break
  
      
      
      