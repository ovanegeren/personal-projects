/*  
https://www.interviewcake.com/question/c/highest-product-of-3

Given an array of integers, find the highest product you can get from three of the integers.

The input arrayOfInts will always have at least three integers.

Bonus Questions:
1. What if we wanted the highest product of 4 items?
2. What if we wanted the highest product of kk items?
3. If our highest product is really big, it could overflow. ↴ How should we protect against this?
*/


#include <stdio.h>
#include <stdlib.h>

#define ARRAY_LEN 10
#define MAX(a, b) ( ((a) > (b)) ? (a) : (b))
#define MIN(a, b) ( ((a) < (b)) ? (a) : (b))

/*
        ATTEMPT #1
*/
/*


int highestProductOfThree(int *arrayOfInts, int array_len){
    int i;
    int top1 = arrayOfInts[0];
    int top2 = arrayOfInts[1];
    int top3 = arrayOfInts[2];
    int current;
    int temp;

    // boundary condition: at exactly 3 return the product of all 3.
    if(array_len == 3){     
        return ((top1 * top2) * top3);
    }    

    //if there are more than 3, go through the remaining array, checking if they are top 3;
    for(i = 3; i < array_len; i++){
        current = arrayOfInts[i];           

        //use consecutive if statements to filter, keeping the 3 hightest out of 4 possible values
        if (current > top1){
            temp = top1;
            top1 = current;
            current = temp;
        }
        if (current > top2){
            temp = top2;
            top2 = current;
            current = temp;
        }
        if (current > top3){
            temp = top3;
            top3 = current;
            current = temp;
        }
    }
    return ((top1 * top2) * top3);
}
*/

/*
didnt consider negative numbers (ie. -10 * -10 = 100, greater than 8 * 9 = 72)
        
        ATTEMPT #2 - (greedy algorithm, O(n) and takes negatives into account but not perfect)
        
*/

// /*
// qsort return value meaning:
// <0 The element pointed by p1 goes before the element pointed by p2
// 0  The element pointed by p1 is equivalent to the element pointed by p2
// >0 The element pointed by p1 goes after the element pointed by p2
// */
// int comp(const void * p1, const void * p2){           //qsort comparator ignores negative values
//     int val1 = abs(*((int *)p1));
//     int val2 = abs(*((int *)p2));
//     return val2 - val1;
// }

// int highestProductOfThree(int *arrayOfInts, int array_len){
//     int i;
//     qsort(arrayOfInts, array_len, sizeof(*arrayOfInts), comp);

//     int top1 = arrayOfInts[0];
//     int top2 = arrayOfInts[1];
//     int top3 = arrayOfInts[2];
//     int product = ((top1 * top2) * top3);
//     // int current;
//     // int p1;
//     // int p2;
//     // int p3;

    
//     // boundary condition: at exactly 3 return the product of all 3.
//     if(array_len == 3){     
//         return product;
//     }    

//     //if there are more than 3, go through the remaining array, checking if they are top 3;
//     for(i = 3; i < array_len; i++){
//         int current = arrayOfInts[i];
        
//         //calculate combinations of products, seeing which is the largest
//         int p1 = (current * top2) * top3;
//         int p2 = (current * top1) * top3;
//         int p3 = (current * top1) * top2;

//         // if 'product' is not the largest value replace it with the larger one
//         if(product != MAX(MAX(MAX(p1,p2),p3),product)){
//             if(p1 == MAX(MAX(p1, p2), p3)){
//                 product = p1;
//                 top1 = current;
//             }else if(p2 == MAX(MAX(p1, p2), p3)){
//                 product = p2;
//                 top2 = current;
//             }else{
//                 product = p3;
//                 top3 = current;
//             }
//         }
//     }
//     return product;
// }

/*
    Self-evaluation:
    This doesn't work (ie. doesnt take negatives into account). Only works if there are 2 negatives in first 2 
*/


/*
        SOLUTION / ATTEMPT #3 (looked up discussion online, code is self-written)

    discussion points learned:
        - solution is not as far from attempt 2 with a few key differences
        - since we're multiply 3 numbers, at least 1 value will always be positive:
            - the largest positive value is always used in the product
            - we're really only searching for 2 values, not 3
*/


/*
qsort return value meaning:
<0 The element pointed by p1 goes before the element pointed by p2
0  The element pointed by p1 is equivalent to the element pointed by p2
>0 The element pointed by p1 goes after the element pointed by p2
*/
int comp(const void * p1, const void * p2){           //qsort comparator ignores negative values
    int val1 = *((int *)p1);
    int val2 = *((int *)p2);
    return val2 - val1;
}

int highestProductOfThree(int *arrayOfInts, int array_len){
    int i;
    qsort(arrayOfInts, array_len, sizeof(*arrayOfInts), comp);      // sorted from + -> -
    int top1 = arrayOfInts[0];      //always used in final product
    int top2 = arrayOfInts[1];
    int top3 = arrayOfInts[2];      
    int product;
    int max_product = (top1 * top2) * top3;         //at least 3 ints guaranteed by question

    if(array_len == 3){
        return max_product;
    }

    for(i=2; i+1<array_len; i++){
        top2 = arrayOfInts[i];
        top3 = arrayOfInts[i+1];
        product = (top1 * top2) * top3;
        if(product > max_product){
            max_product = product;
        }
    }
    return max_product;
}



int main(){
    int arrayOfInts[ARRAY_LEN] = {12, 2, 3, 11, 5, 6, -14, -15, 9, 10};
    int highest_product = highestProductOfThree(arrayOfInts, ARRAY_LEN);
    printf("highest product: %d\n", highest_product);
    //debug
    printf("Ints: {%d, %d, %d, %d, %d, %d, %d, %d, %d, %d}",arrayOfInts[0],
                                                            arrayOfInts[1],
                                                            arrayOfInts[2],
                                                            arrayOfInts[3],
                                                            arrayOfInts[4],
                                                            arrayOfInts[5],
                                                            arrayOfInts[6],
                                                            arrayOfInts[7],
                                                            arrayOfInts[8],
                                                            arrayOfInts[9]);
    return 0;
}





