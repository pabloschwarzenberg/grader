numerodetelefono = int(input("Ingrese número telefónico con 8 cifras : "))
horadelallamada = int(input("ingrese hora de la llamada como número entero entre 0 y 23 : "))

if horadelallamada >= 0 and horadelallamada <= 7:
    print("Contestar, puede ser una emergencia")

if horadelallamada <= 14:
    print("No contestar excepto si el número termina con 909")
   
if horadelallamada >= 17 and horadelallamada <= 19:
    print("Contestar. No contestar exceptuando un número que comienza con 877")

if horadelallamada > 19:
    print("No contestar el celular")