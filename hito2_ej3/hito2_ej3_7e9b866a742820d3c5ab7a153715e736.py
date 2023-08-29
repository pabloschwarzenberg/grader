main()

{

int num,pares,impares,r;
pares=0;

impares=0;

r=0;

printf("Ingrese Numero: ");

scanf("%d",&num);

for(int i=1;i<=num;i++)

{
if(i%2==0)

{

s='^';

s2='2';

s3='+';

impares=impares-i*i;

}
else
{

s='^';

s2='2';

s3='-';

pares=pares+i*i;
}
if(i==num)
 {
s='^';
s2='2';
3='=';
}
printf("%d%c%c%c",i,s,s2,s3);
}
r=pares+impares;
printf("%s%d","\n",r);
getch();
return 0;
}print(matriz[x,-x-1])