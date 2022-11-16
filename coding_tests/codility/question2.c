// you can write to stdout for debugging purposes, e.g.
// printf("this is a debug message\n");
#include <string.h>
#include <stdlib.h>
#include <stddef.h>
#include <stdio.h>

char * player(char *S, int A[], int N, char * msg);
int k = 0;


char * solution(char *S, int A[], int N) {
    char * message = (char *) malloc(N * sizeof(char));
    message = "";
    return player(S, A, N, message);
}

char * player(char *S, int A[], int N, char * msg) {
    // static int k = 0;
    printf("k = %d, string = %s\n", k, msg);
    //exit condition
    if(A[k] == 0){
        return msg;
    }

    printf("A[k] = %d\n", A[k]);
    printf("S[k]=%c\n", S[k]);
    msg = strncat(msg, &S[k], 1);
    // msg = &S[k];
    printf("msg=%s\n", msg);
    k = A[k];
    return player(S, A, N, msg);
}