#include <stdio.h>

int main () {
    int num1;
    int num2;
    printf("Inserisci il primo numero");
    scanf("%d" , &num1);
    printf("Inserisci il secondo numero");
    scanf("%d" , &num2);
    int somma = num1 + num2;
    printf("Somma: %d\n" , somma);
    int media = somma / 2;
    printf("Media : %d\n" , media);
    
    return 0;
}