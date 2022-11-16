#include <stddef.h>
#include <assert.h>
#include <stdlib.h>
#include <string.h>

  typedef struct BinaryTreeNode {
    void *value;
    struct BinaryTreeNode *left;
    struct BinaryTreeNode *right;
} BinaryTreeNode;

BinaryTreeNode * binaryTreeNodeNew(const void *value, size_t valueSize)
{
    BinaryTreeNode *node;

    node = malloc(sizeof(BinaryTreeNode));
    assert(node != NULL);

    node->value = malloc(valueSize);
    assert(node->value != NULL);
    memcpy(node->value, value, valueSize);

    node->left = NULL;
    node->right = NULL;

    return node;
}

BinaryTreeNode * binaryTreeNodeInsertLeft(BinaryTreeNode *treeRoot, const void *value, size_t valueSize)
{
    treeRoot->left = binaryTreeNodeNew(value, valueSize);
    return treeRoot->left;
}

BinaryTreeNode * binaryTreeNodeInsertRight(BinaryTreeNode *treeRoot, const void *value, size_t valueSize)
{
    treeRoot->right = binaryTreeNodeNew(value, valueSize);
    return treeRoot->right;
}

void binaryTreeNodeFree(BinaryTreeNode *treeRoot)
{
    if (treeRoot != NULL) {
        binaryTreeNodeFree(treeRoot->left);
        binaryTreeNodeFree(treeRoot->right);
        free(treeRoot->value);
        free(treeRoot);
    }
}