TAM_MAX_CLAVE = 26

 4.         

 5. def obtenerModo():

 6.     while True:

 7.         print('¿Deseas encriptar o desencriptar un mensaje?')

 8.         modo = input().lower()

 9.         if modo in 'encriptar e desencriptar d'.split():

10.             return modo

11.         else:

12.             print('Ingresa "encriptar" o "e" o "desencriptar" o "d"')

13.

14. def obtenerMensaje():

15.     print('Ingresa tu mensaje:')

16.     return input()

17.

18. def obtenerClave():

19.     clave = 0

20.     while True:

21.         print('Ingresa el número de clave (1-%s)' % (TAM_MAX_CLAVE))

22.         clave = int(input())

23.         if (clave >= 1 and clave <= TAM_MAX_CLAVE):

24.             return clave

25.

26. def obtenerMensajeTraducido(modo, mensaje, clave):

27.     if modo[0] == 'd':

28.         clave= -clave

29.     traduccion = ''

30.

31.     for simbolo in mensaje:

32.         if simbolo.isalpha():

33.             num = ord(simbolo)

34.             num += clave

35.

36.             if simbolo.isupper():

37.                 if num > ord('Z'):

38.                     num -= 26

39.                 elif num < ord('A'):

40.                     num += 26

41.             elif simbolo.islower():

42.                 if num > ord('z'):

43.                     num -= 26

44.                 elif num < ord('a'):

45.                     num += 26

46.

47.             traduccion += chr(num)

48.         else:

49.             traduccion += simbolo

50.     return traduccion

51.

52. modo = obtenerModo()

53. mensaje = obtenerMensaje()

54. clave = obtenerClave()

55.

56. print('Tu texto traducido es:')

57. print(obtenerMensajeTraducido(modo, mensaje, clave))