#Descomponer un número
main()
{
   int x, y, u, d, c;
   printf ("x = ");
   scanf ("%d",&x);
   u = x % 10;
   printf ("%d unidades",u);
   
   y = x - u;
   y = y % 100;
   d = y/10;
   printf ("\n%d decenas",d);
   
   y = x - d*10 -u;
   c = y/100;
   printf ("\n%d. centenas",c);
   
   getch();  
}