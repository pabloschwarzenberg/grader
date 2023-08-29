#Cálculo del dígito verificador de un rut
rut=int(input(" rut: "))
one =(rut//10000000)     * 3
two = ((rut//1000000)%10) * 2
three = ((rut//100000)%10)  * 7
four = ((rut//10000)%10)   * 6
five = ((rut//1000)%10)    * 5
six = ((rut//100)%10)     * 4
seven = ((rut//10)%10)      * 3
eight = ((rut//1)%10)       * 2
sumas = (one + two +three + four + five + six + seven + eight)
resta_1 = sumas // 11
resta_2 = sumas -(11*resta_1)
resta_total = 11-resta_2
if resta_total == 11:
  print("dv=",end="")
  print(0)

elif resta_total == 10:
  print("dv=",end="")
  print("k")
else:
  print("dv=",resta_total)
  print("dv=",end="")