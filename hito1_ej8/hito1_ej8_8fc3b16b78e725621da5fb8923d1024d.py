#Descomponer un número
int numero = 0 ;

  print( " Escribe un numero \ n " );

  int millares = numero / 1000 ;
  int centenas = (numero- (millares * 1000 )) / 100 ;
  int decenas = (numero- (millares * 1000 + centenas * 100 )) / 10 ;
  int unidades = numero- (millares * 1000 + centenas * 100 + decenas * 10 );

  print ( " Millares = % i \ n " , millares);
  print ( " Centenas = % i \ n " , centenas);
  print ( " Decenas = % i \ n " , decenas);
  print ( " Unidades = % i \ n " , unidades);