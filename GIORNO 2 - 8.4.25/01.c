#include<stdio.h>
int main () {

int num1;
int num2;

printf("Inserisci il primo numero: ");
scanf("%d", &num1);

printf("\nInserisci il secondo numero: ");
scanf("%d", &num2);

int moltiplica = num1 * num2;
printf("\nIl risultato è: %d\n", moltiplica);

printf("*************\n");
return main ();
}