if name=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
def NumeroPerfecto(num):
 suma = 0
 for i in range(1,num):
  if (num % (i) == 0):
   suma += (i)
  if num == suma:
  return True
 else:
  return False
num = int(raw_input("ingrese un numero: "))
if NumeroPerfecto(num):
 print("%s es n° perfecto" % num)
else:
 print("%s NO es n° perfecto" % num)