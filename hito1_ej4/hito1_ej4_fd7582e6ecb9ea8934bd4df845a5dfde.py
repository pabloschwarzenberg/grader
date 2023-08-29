#Conversión de Decimal a Binario
def main(x):

    
    {
    int x, bin[999]
    int i = 0
    
    printf("Ingresa un numero decimal: ");
    scanf("%i",&n);

    while (n != 0)
    {
          bin[i] = n % 2;
          n = n / 2;
         i++;
    }
    
    i--;
    
    printf("Binario: ");   

    while (i>=0)
    {
          printf("%i",bin[i]);
          i--;
    }
    
	return 0;
}
