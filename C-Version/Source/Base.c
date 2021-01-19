#include <stdio.h>
#include <stdlib.h>

int main(void)
{
unsigned long N, tnumber, Q, B, R;
unsigned char digit, index, length, counter, value[1024], M[1024];
printf(" _______________________________________________________________\n");
printf("| In the Name of Allah, the Most Gracious and the Most Merciful |\n");
printf("| Program by Muhammad Omar Farooq 20-CP-33                      |\n");
printf("| Department of Computer Engineering                            |\n");
printf("| University of Engineering and Technology, Taxila              |\n");
printf("|_______________________________________________________________|\n\n");

printf("Enter number: ");
scanf("%lu", &N);

printf("Enter base: (greater than 1 and less than 37): ");
scanf("%lu", &B);

if (B < 2 || B >36)
{
    printf("Base should be between 2 and 36.\n");
    exit(0);
}

Q = N;
tnumber = N;
index = 0;
while(Q >= B)
{
   Q = tnumber/B;
   R = tnumber % B;

   if(R < 10)
      digit = R + '0';

   if((B > 10) && (R > 9))
      digit = 'A' + R - 10;

   value[index++] = digit;
   tnumber = Q;
}
if (Q < 10)
   digit = Q + '0';
else
   digit = 'A' + Q - 10;

value[index++] = digit;
value[index] = '\0';

counter = 0;
length = index;
while(counter <= index)
{
   M[counter] = value[--length];
   counter++;
}
M[counter]=0;

printf("\n");
printf("Number %lu in base %lu is %s.\n", N, B, M);
getch();
return 0;
}
