**Problem 4.** Consider the following algorithm for testing if a given binary tree has the binary search tree property. 

```python
def test_bst(T):
	for u ∈ T do 
		if u.left != NULL and u.key < u.left.key then 
			return False
		if u.right != NULL and u.key > u.right.key then 
			return False
	
	return True
```

Either prove the correctness of this algorithm or provide a counter example where it fails to return the correct answer.

a binary tree is a tree data structure in which each node has at most two children, which are referred to as the left child and the right child. where the left child is lesser than (or equal to in some cases) the parent and the right child is greater than the parent

this goes through every node in the tree and checks to ensure that this property remains true for every child node. if the parent node is larger than the left child, then the binary seach is incorrect. if right is smaller than parent.  

**Problem 5**. Consider the following operation on a binary search tree: largest() that returns the largest key in the tree. Give an implementation that runs in O(h) time, where h is the height of the tree. 

keep recursing on the right node of the binary tree

```python
def largest(node):
	if node.right == NULL
		return node

	largest(node.right)

def largest_iter(node):
	while (node.right != NULL):
		node = node.right

	return node
```

Since in a binary search tree we have that for every node u u.le f t.key < u.key < u.right.key, the above algorithm correctly finds the largest key in the tree.

it follows the binary seach property that larger nodes are on the right

The algorithm clearly runs in O(h) time, as it takes O(1) time per level of the tree it visits.

**Problem 6**. Consider the following operation on a binary search tree: secondlargest() that returns the second largest key in the tree. Give an implementation that runs in O(h) time, where h is the height of the tree. 

```python
def largest(node):
	if node.right == NULL
		return node

	largest(node.right)

def second_largest(root):
	largest_node = largest(root)

	if largest.left != NULL
		return largest(largest.left)
	else 
		return largest_node.parent
```

First we find the node w holding the largest key in the tree. If w has a left child, then the second largest key must be in this subtree, so we again search for the largest key in w.left. 

Otherwise, the second largest key can be found at w’s parent, provided that w has a parent, i.e., w is not the root of the tree. If w is the root of the tree and its left subtree is empty, then w is the only node in the tree and so the second-largest element is not defined and we can throw an exception. 

The correctness follows from the binary search tree property. After finding the largest key, the second largest key is either its parent or the largest value in its left subtree. Since we know that every key in the left subtree of w is larger than the key of w’s parent, the choice of the algorithm follows. If w has no left subtree, we know that there are no keys between w and its parent, as all keys in the left subtree of w’s parent and those higher up in the tree are smaller than w’s parent’s key by the binary search tree property. 

Since the algorithm takes O(1) time per level of the tree it visits, the total running time is O(h).

**Problem 7**. Consider the following operation on a binary search tree: median() that returns the median element of the tree (the element at position ⌊n/2⌋ when considering all elements in sorted order). Give an implementation that runs in O(h), where h is the height of the tree. You are allowed to augment the insertion and delete routines to keep additional data at each node.

We can augment the nodes in our binary search trees with a size attribute. For a node u, u.size is the number of nodes in the subtree rooted at u. When inserting a new key at some node w, we only need to increase by 1 the size of ancestors of w, which takes O(h) time. Similarly, when we delete a node w with at least one external child, we only need to decrease by 1 the size of ancestors of w. Hence, the insertion and deletion times remain the same. 

you make all nodes keep a size attribute. for every node in the tree, you have the size of the subtree rooted at u. 

whenever something is inserted, you would increase the size 1 to the nodes as are traversing. (or you would calculate it upwards) after you have already inserted it. Similarly you would delete and deduct the size

We implement a more powerful operation called position(k), which returns the kth key (in sorted order) stored in the tree. When searching for the kth element at some node u, we check if u.left.size ≥ k in which case we know that the kth element is in the left subtree and we search for the kth key in u.left. Otherwise, if u.left.size = k − 1, the kth key is at the root u. Finally, if u.left.size < k − 1, then we know that the kth element is in the right subtree, so we search for the (k − u.left.size − 1)th key there, i.e., k minus the number of nodes smaller than the root of u.right.key. 

????

The complexity is O(h) because we do O(1) work at each node and we only traverse one path from the root to the element we are searching for.

**Problem 8**. Consider the following binary search tree operation: remove all(k1, k2) that removes from the tree any key k ∈ [k1, k2]. Give an implementation of this operation that runs in O(h + s) where h is the height of the tree and s is the number of keys we are to remove.

