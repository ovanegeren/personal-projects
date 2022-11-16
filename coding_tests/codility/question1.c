// you can write to stderr for debugging purposes, e.g.
// fprintf(stderr, "this is a debug message\n");
#include <math.h>
#include <stdio.h>

void solution(int N) {
    // write your code in C99 (gcc 6.2.0)
    int exp = 0;
    int powOf2 = (int) pow(2, exp++);
    int i;

    for(i=1; i<=N; i++){
        if(i == powOf2){
            //increment
            powOf2 = (int) pow(2, exp++);
            printf("POWER\n");
        }else{
            printf("%d\n", i);
        }
        //iterate through N printing
    }
}


int main(){
    solution(1000);
    return 0;
}