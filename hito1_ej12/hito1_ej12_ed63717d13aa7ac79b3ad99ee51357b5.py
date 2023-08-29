import random

num_secreto= random.randrange(1000,9999)
turno=1
gana=0
while turno<=4:
  print("turno", turno)
  n=int(input("ingrese el numero para adivinar: "))
  if n>=1000 and n<=9999:
    if num_secreto==n:
      print("FELICITACIONES, has acertado en", turno, "turnos")
      turno=10000
      gana==1
    else:
      while num_secreto>0:
        if (num_secreto%10==n%10):
          print(num_secreto%10, "es fama")
        n=n//10
        num_secreto=num_secreto//10
  turno=turno+1
  if gana +=1:
    print("fin del juego, la secuencia era", num_secreto)