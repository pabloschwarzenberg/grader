#Descomponer un número
  int  main ( void ) {

	int numero = 0 ;
	
	printf ( " Escribe un numero \ n " );
	scanf ( " % i " , & numero);

	// ////// Obtener las unidades, decenas, centenas ////////	
	int millares = numero / 1000 ;
	int centenas = (numero- (millares * 1000 )) / 100 ;
	int decenas = (numero- (millares * 1000 + centenas * 100 )) / 10 ;
	int unidades = numero- (millares * 1000 + centenas * 100 + decenas * 10 );

	printf ( " Millares = % i \ n " , millares);
	printf ( " Centenas = % i \ n " , centenas);
	printf ( " Decenas = % i \ n " , decenas);
	printf ( " Unidades = % i \ n " , unidades);    