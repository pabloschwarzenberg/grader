#Factores Primos
NumeroUsuario = int(input("Ingrese un numero: "))
i = 2
while i <= NumeroUsuario:
     if NumeroUsuario%i==0:
       print(i)
       NumeroUsuario = NumeroUsuario//i
      
     else:
      i = i +1