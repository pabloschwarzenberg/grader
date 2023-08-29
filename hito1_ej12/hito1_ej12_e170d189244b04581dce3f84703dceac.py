#Juego adivina mi número
 # Este es el juego de adivinar el número.

 2. import random

 3.

 4. intentosRealizados = 0

 5.

 6. print('¡Hola! ¿Cómo te llamas?')

 7. miNombre = input()

 8.

 9. número = random.randint(1, 20)

10. print('Bueno, ' + miNombre + ', estoy pensando en un número entre 1 y 20.')

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

27.

28. if estimación == número:

29.     intentosRealizados = str(intentosRealizados)

30.     print('¡Buen trabajo, ' + miNombre + '! ¡Has adivinado mi número en ' + intentosRealizados + ' intentos!')

31.

32. if estimación != número:

33.     número = str(número)

34.     print('Pues no. El número que estaba pensando era ' + número)      