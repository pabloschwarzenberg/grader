import random
n = random.randint(1,20)
a = eval(input("Adivine número: "))

if a==n:
          print("Adivinaste, mi número era ",a)
else:
          print("No adivinaste, intenta de nuevo")
          b = eval(input("Adivine número: "))
          if b==n:
              print("Adivinaste, mi número era ",b)
          else:
              print("No adivinaste, intenta de nuevo")
              c = eval(input("Adivine número: "))
              if c==n:
                  print("Adivinaste, mi número era ",c)
              else:
                  print("No adivinaste, intenta de nuevo")
                  d = eval(input("Adivine número: "))
                  if d==n:
                      print("Adivinaste, mi número era ",d)
                  else:
                      print("No adivinaste, intenta de nuevo")
                      e = eval(input("Adivine número: "))
                      if e==n:
                          print("Adivinaste, mi número era ",e)
                      else:
                          print("No adivinaste, mi número era ",n)