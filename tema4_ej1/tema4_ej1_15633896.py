lista=["tropical","pescado","murcielago","avion","teclado","libros","flores"]
import random
lista_palabra=random.randint(1,7)
palabra=lista[lista_palabra]
palabra_secreta=palabra
longitud=len(palabra)
cantidad=random.randint(1,longitud)
posiciones_escogidas=[]
letras_ocultas=[]
lista2=[]


def ocultar_letras(palabra,cantidad):
   i=0
   a=0
   b=0

   while i<cantidad:
        posicion_aleatoria=random.randint(1,longitud)
        if posicion_aleatoria!=a:
           a=posiciones_escogidas
           posiciones_escogidas.append(posicion_aleatoria)
           i=i+1
        else:
           i=i

   for cada_posicionescogida in posiciones_escogidas:
      cada_posicionescogida=b
      letra_escogida=palabra[b+1]
      palabra=palabra.replace(letra_escogida,"_")
      

   return(palabra)

      


def revisar_letra(palabra_secreta,palabra,letra):
   n=0
   
   while n<7:
      
      numero=palabra_secreta.find(letra)
      if numero!=-1:

         for i in palabra:
            posicioncadacosa=palabra.find(i)
            if i=="_":
               a=palabra_secreta[posicioncadacosa]
               if a==letra:
                  palabra=palabra.replace(i,letra)
                  
      
      n=n+1

   return palabra
               