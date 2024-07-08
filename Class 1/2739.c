/*
Date: 2024.07.07
No: 2739
Tier: Bronze 5
Name: 구구단
Language: C
*/

#include<stdio.h>

int main(){
    int a;
    scanf("%d", &a);
    for(int i = 1; i <= 9; i++)
    	printf("%d * %d = %d \n", a, i, a*i);
    return 0;
}