#Juego adivina mi número
      
 intentosRealizados = 0



print('¡Hola! ¿Cómo te llamas?')

 miNombre = input()



numero = random.randint(1, 20)
¿ print('Bueno, ' + miNombre + ', estoy pensando en un número entre 1 y 20.')

11.

12. while intentosRealizados < 6:

13.     print('Intenta adivinar.') # Hay cuatro espacios delante de print.

14.     estimación = input()

15.     estimación = int(estimación)

16.

17.     intentosRealizados = intentosRealizados + 1

18.

19.     if estimación < número:

20.         print('Tu estimación es muy baja.') # Hay ocho espacios delante de print.

21.

22.     if estimación > número:

23.         print('Tu estimación es muy alta.')

24.

25.     if estimación == número:

26.         break



 if estimación == número:

    intentosRealizados = str(intentosRealizados)

   print('¡Buen trabajo, ' + miNombre + '! ¡Has adivinado mi número en ' + intentosRealizados + ' intentos!')


 if estimación != número:

    número = str(número)

    print('Pues no. El número que estaba pensando era ' + número)