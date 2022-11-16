/*
https://www.interviewcake.com/question/c/balanced-binary-tree

PROMPT:
Write a function to see if a binary tree ↴ is "superbalanced" (a new tree property we just made up).

A tree is "superbalanced" if the difference between the depths of any two leaf nodes ↴ is no greater than one.

Here's a sample binary tree implementation:

*/
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

int balancedBinaryTree(BinaryTreeNode *treeRoot){

}
/*
GOTCHAS:
Your first thought might be to write a recursive function, thinking, "the tree is balanced if the left subtree is balanced and the right subtree is balanced." 
This kind of approach works well for some other tree problems.

But this isn't quite true. Counterexample: suppose that from the root of our tree:

The left subtree only has leaves at depths 10 and 11.
The right subtree only has leaves at depths 11 and 12.
Both subtrees are balanced, but from the root we will have leaves at 3 different depths.

We could instead have our recursive function get the array of distinct leaf depths for each subtree. 
That could work fine. But let's come up with an iterative solution instead. 
It's usually better to use an iterative solution instead of a recursive one because it avoids stack overflow.

We can do this in O(n)O(n) time and O(n)O(n) space.

What about a tree with only one leaf node? Does your function handle that case properly?
*/

/*
SOLUTION: *missing*
*/

/*
COMPLEXITY:
O(n) time and O(n)O(n) space.

For time, the worst case is the tree is balanced and we have to iterate over all nn nodes to make sure.

For the space cost, we have two data structures to watch: depths and nodes.

depths will never hold more than three elements, so we can write that off as O(1)O(1).

Because we’re doing a depth first search, nodes will hold at most dd nodes where dd is the depth of the tree 
(the number of levels in the tree from the root node down to the lowest node). So we could say our space cost is O(d)O(d).

But we can also relate dd to nn. In a balanced tree, dd is O(\log_{2}(n))O(log 
2
​
 (n)). And the more unbalanced the tree gets, the closer dd gets to nn.

In the worst case, the tree is a straight line of right children from the root where every node in that line also has a left child.
The traversal will walk down the line of right children, adding a new left child to nodes at each step. 
When the traversal hits the rightmost node, nodes will hold half of the nn total nodes in the tree. 
Half n is O(n)O(n), so our worst case space cost is O(n)O(n).
*/