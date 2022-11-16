/*
    for detailed explaination, see:
    https://www.interviewcake.com/c-interview-questions
*/


#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include <string.h>

  char * strReplace(const char *src, const char *old, const char *new)
{
    size_t newLen = 0;
    char *srcSuffix = NULL;

    // get memory to hold dst
    size_t dstLen = strlen(src) - strlen(old) + strlen(new);
    char *dst = malloc(sizeof(char) * (dstLen + 1));  // +1 for NUL terminator
    char *dstOffset = dst;
    assert(dst != NULL);

    // copy src up to old (prefix) into dst
    char *oldInSrc = strstr(src, old);
    size_t prefixLen = oldInSrc - src;

    strncpy(dstOffset, src, prefixLen);
    dstOffset += prefixLen;

    // copy new into dst
    newLen = strlen(new);
    strncpy(dstOffset, new, newLen);
    dstOffset += newLen;

    // find suffix start in src
    srcSuffix = oldInSrc + strlen(old);
    // copy suffix into dst
    strcpy(dstOffset, srcSuffix);

    return dst;
}




int main(){

char *dst = strReplace("My favorite language is Python", "Python", "C");
print("%s", dst);

}