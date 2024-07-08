/*
Date: 2024.07.07
No: 10869
Tier: Bronze 5
Name: 사칙연산
Language: C
*/

#include<stdio.h>

int main(){
    int a, b;
    scanf("%d %d", &a, &b);
    printf("%d\n", a+b);
    printf("%d\n", a-b);
    printf("%d\n", a*b);
    printf("%d\n", a/b);
    printf("%d", a%b);
    return 0;
}