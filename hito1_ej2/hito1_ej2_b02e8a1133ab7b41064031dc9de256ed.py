#Contestador de celular
#Contestador de celular
#El programa debe preguntar al usuario por la hora del día y por el número de celular que llama
#Imprimir “CONTESTAR” o “NO CONTESTAR” en pantalla
#El número telefónico debe ser representado por un número entero (int) de 8 cifras (por ejemplo 78735653)
numero=str(int(input("Digite numero de telefono: ")))
if len(numero)!= 8:
    print("Numero de telefono invalido")
    
#Mientras que la hora es representada por un número entero entre 0 y 23
hora=int(input("Ingrese hora de llamada: "))

#Si la llamada ocurre entre 00:00 y 07:00, la contestas ya que podría ser una emergencia.
while True:
    if hora > 0 and hora < 7:
        print("NO CONTESTAR")
        break
    
#Si ocurre antes de las 14:00 no la contestas, excepto si el número termina en 909.
    if hora < 14:
        print("CONTESTAR")
        break
    if numero.find("909",5,7):
        print("NO CONTESTAR")
        break
#Durante la tarde, solamente contestas entre 17:00 y 19:00, exceptuando un número que comienza por 877.
    if hora > 17 and hora < 19:
        print("NO CONTESTAR")
        break
    if numero.find("877",0,2):
        print("CONTESTAR")
        break
#Después de las 19:00, no contestas el celular.
    if hora > 19 and hora < 23:
        print("CONTESTAR")
        break
      