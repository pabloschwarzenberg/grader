#Descomponer un número
a=int(input())
int millares=a/1000;
int centenas=(a-(millares*1000))/100;
int decenas=(a- (millares*1000 + centenas*100))/10;
int unidades=a-(millares*1000 + centenas*100 + decenas*10 );

printf("Millares= %i\n", M);
printf("Centenas= %i\n", C);
printf("Decenas= %i\n", D);
printf("Unidades= %i\n", U);
