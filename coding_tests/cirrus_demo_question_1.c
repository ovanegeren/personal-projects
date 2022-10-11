
/* PROMPT:
This is a demo task.

Write a function:

int solution(int A[], int N);

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
*/


/* ----- ATTEMPT #1 ------- */
// #include <stdbool.h>

// int solution(int A[], int N) {
//     int i = 0;
//     int num = 1;
//     bool num_present = false;

//     while(true){
//         while (i < N){                  //search for present number
//             if(num == A[i]){
//                 num_present = true;
//                 break;
//             }
//             i++;
//         }
//         i = 0;

//         if(num_present){                //if number is present, increment number and reset the search
//             num_present = false;
//             num++;
//             continue;
//         }else{
//             return num;                     //if number is not present, solution found
//         }

//     }
// }


/* ----- ATTEMPT #2 ------ */
#include <stdlib.h>


int comp (const void * elem1, const void * elem2);

int solution(int A[], int N)
{
    qsort(A, N, sizeof(*A), comp);
    int i = 0;
    while(A[i] <= 0){             // find the first element in sorted array > 0    
        i++;
    }
    if(A[i] > 1){
        return 1;
    }else{
        while(i+1 < N){
            if(A[i+1] > (A[i] + 1)){
                return A[i] + 1;
            }
            i++;
        }
        return A[i] + 1;
    }

}

int comp (const void * elem1, const void * elem2)
{
    int int1 = *((int*)elem1);
    int int2 = *((int*)elem2);
    if (int1 > int2)
        return 1;
    if (int1 < int2)
        return -1;
    return 0;
}