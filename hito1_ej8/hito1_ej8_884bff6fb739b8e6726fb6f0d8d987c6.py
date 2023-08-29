#Descomponer un número
int main(void){

int numero=0;

printf("Escribe un numero\n");
scanf("%i",&numero);

#////////Obtener las unidades,decenas,centenas////////	
int millares=numero/1000;
int centenas=(numero-(millares*1000))/100;
int decenas=(numero- (millares*1000 + centenas*100))/10;
int unidades=numero-(millares*1000 + centenas*100 + decenas*10 );

print("Millares= %i\n", millares);
print("Centenas= %i\n", centenas);
print("Decenas= %i\n", decenas);
print("Unidades= %i\n", unidades);