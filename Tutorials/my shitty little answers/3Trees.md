 Problem 3. Design a linear time algorithm that given a tree T computes for every node u in T the size of the subtree rooted at u.

first use a search algorithm binary to return the 

```python
def get_sizeof_subtree(current_vertex, size):
	size = 1; # count itself

	#go through all children and count its children
	for child in current vertex:
		size += get_sizeof_subtree(child, size);

	return size;
```

**PROOF OF CORRECTNESS**

Correctness: because this is a recursive algorithm we can attempt to use a proof by induction to prove correctness

INDUCTIVE HYPOTHESIS: the function will get the correct size of the subtree

BASE CASE: the current vertex has no children and thus will not call the function get size of subtree and will return 1 (because the only thing in the subtree is itself)

**proof**
- assume that the inductive hypothesis holds true for node a that has k elements in the subtree
- then assume that node a has a parent b, the parent will have k + 1 elements total
- because node a will return the corrent number of elements (assumed from the IH), b will simply include itself in the size adding 1 to the total later. when a returns k. b will return k + 1

**running time**

the running time will come from how many children are there in total. O(n)

because every child will call its own children which are inturn children of u in total. 

**Problem 4.** In a binary tree there is a natural ordering of the nodes on a given level of the tree, i.e., the left-to-right order that you get when you draw the tree. Design an algorithm that given a tree T and a level k, visits the nodes in level k in this natural order. Your algorithm should perform the whole traversal in O(n) time.

```python

def level_print(tree, level):
	level_print(tree.root, 0, level)

def level_helper(node, current_level, level):
	if node == NULL
		return;

	current_level++;

	if current_level == level - 1:
		if node.left != NULL 
			print(node.left)
		if node.right != NULL 
			print(node.right)
	else
		level_helper(node.left, current_level, level)
		level_helper(node.right, current_level, level)

def level_getter(node, level):
	current_level = 0;
	current_node = NULL
	while current_level != level:
		current_node = current 

```

**Problem 5** Design an algorithm that given a binary tree T and a node u, returns the node that would be visited after u in a pre-order traversal. Your algorithm should not compute the full traversal and then search for u in that traversal. 

do a pre-order traversal and check for u. if u is left then take the right, if u is right then take the parent. pre-order would take O(n) time

if u is left then follow a path left till it hits another one

**Problem 6** Design an algorithm that given a binary tree T and a node u, returns the node that would be visited after u in an in-order traversal. Your algorithm should not compute the full traversal and then search for u in that traversal. 

if node u is a left then 

**Problem 7** Design an algorithm that given a binary tree T and a node u, returns the node that would be visited after u in a post-order traversal. Your algorithm should not compute the full traversal and then search for u in that traversal. 

**Problem 8** The balance factor of a node in a binary tree is the absolute difference in height between its left and right subtrees (if the left/right subtree is empty we consider its height to be -1). Design an algorithm for computing the balance factor of every node in the tree in O(n) time

```python
calculate_balance_factor(node, 0)

def calculate_balance_factor(node, current_level):
	current_level++

	if node.left == NULL 
		node.balance_factor = -1
		return current_level
	if node.right == NULL
		node.balance_factor = -1
		return current_level
	
	node.balance_factor = abs(calculate_balance_factor(node.left, current_level) - calculate_balance_factor(node.right, current_level))
```

**base case:** when there is no more to get through that means the current height has been reached. and thus will return it the max depth

**inductive hypothesis:** assume that the calculate balance factor will return the correct balance factor

**proof of correctness**
- assume that the inductive hypothesis holds true for node a that has k elements in the subtree
- then assume that node a has a parent b, the parent will have k + 1 elements total
- because node a will return the corrent number of elements (assumed from the IH), b will simply include itself in the size adding 1 to the total later. when a returns k. b will return k + 1

**Problem 9** Describe an algorithm for performing an Euler tour traversal of a binary tree that runs in linear time and does not use a stack or recursion



**Problem 10** For any pair of nodes in a tree there is a unique simple path (one that does not repeat vertices) connecting them. Design a linear time algorithm that finds the longest such path in a tree.

