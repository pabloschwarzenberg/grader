var1 = input("Ingrese el valor de la variable 1: ")
var2 = input("Ingrese el valor de la variable 2: ")
var3 = input("Ingrese el valor de la variable 3: ")

if(var1 < var2 < var3):
  print(var1,",",var2,",",var3)
if(var2 < var3 < var1):
  print(var2,",",var3,",",var1)
if(var3 < var1 < var2):
  print(var3,",",var1,",",var2)
if(var1 < var3 < var2):
  print(var1,",",var3,",",var2)
if(var2 < var1 < var3):
  print(var2,",",var1,",",var3)
if(var3 < var2 < var1):
  print(var3,",",var2,",",var1)
if(var1 == var2 < var3):
  print(var1,",",var2,",",var3)
if(var1 == var3 < var2):
  print(var1,",",var3,",",var2)
if(var2 < var1 == var3):
  print(var2,",",var1,",",var3)