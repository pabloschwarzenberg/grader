
#include <iostream>
#include <conio>
void main()
{int a,b,c,aux;
clrscr();
cout<<"ingrese los tres datos:";
cin>>a;
cin>>b;
cin>>c;
if(a<b)
{aux=a;
a=b;
b=aux;
}
if(a<c)
{aux=a;
a=c;
c=aux;
}
if(b<c)
{aux=b;
b=c;
c=aux;
}
cout<<"los datos ordenados son:";
cout<<a<<""<<b<<""<<c;
getch();
}
