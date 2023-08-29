def jerigonzo(string):
	
	jerigonzo = ''
	vocales = 'aeiouAEIOU'

	for letra in string:
		
		jerigonzo+=letra
	
		if letra in vocales:
			
			jerigonzo+='p'+letra.lower()

	return jerigonzo

if __name__=='__main__':

    string=input('Ingresa un texto: ')
    jerigonzo=jerigonzo(string)
    print('')
    print('texto traducido a jerigonzo:', jerigonzo)
         