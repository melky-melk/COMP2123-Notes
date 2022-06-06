# ADT
Abstract data types are used to represent more a concept or an idea, with no regard for implementation

Say, using a stack. a stack is an abstract type because it has the idea of popping and pushing. but it doesnt say how to implement it. because it can be implemented in many ways. like using arrays that change size, or it can use a linked list that tracks where the head is currently. 

**A data structure** is a concrete representation of data, and this is from the point of view of an implementer, not a user

most of the time, using a linked list is doubly linked

# Trees
a tree is a graph that is connected and has no cycles

## Terminology

- to make things easier, all the leaves will have 2 children that will be null

| Term                | Description                                                                  |
| ------------------- | ---------------------------------------------------------------------------- |
| root                | the first node at the beginning of the tree                                  |
| internal node       | nodes with at least one child                                                |
| leaf/external nodes | node without children (or represented with both children as NULL)            |
| ancestors           | the parents                                                                  |
| descendants         | a child                                                                      |
| depth of a node     | how far down the node is the number of ancestors it has not including itself |
| level               | the set of nodes at a given depth                                            |
| height of a tree    | the max depth                                                                |
| Subtree             | tree made up of node and some decendents                                     |
| edge                | pair of nodeswhere one is a parent of another                                |
| path                | sequence of nodes that would lead from one to another                        |
| forest              | a bunch of trees together, unconnected from other trees                                                                           |

## Traversals
![[Pasted image 20220602202802.png]]

### Preorder Traversal Example
keeps following a path to attempt to going to the left untill it cannot left anymore
![[Preorder-traversal.gif]]
**explores the left subtree first, then the right** 

- keeps following a path to attempt to going to the left untill it cannot left anymore
- in that case it would go back up to its parent and go to the right
- in the case where there is no more to be traversed it would go all the way up

### Postorder Traversal
will always try to get the left most element if possible
![[Postorder-traversal.gif]]

### Inorder Traversal
left, parent, right.
this will be in ascending order in a binary tree

![[Inorder-traversal.gif]]

![[Pasted image 20220602204222.png]]

to find an element within a binary search tree, you compare the value of the node to the value you are searching for, if it is more than, then go to the right, if it is less than then go to the left

when inserting you do the same, and follow the path

# Hash Functions
Hash functions try to create a number as random as possible so it can insert it into an array with as little collision a possible. they wrap around using modulo. the array should be pretty big 

linear chaining top, probing bottom
![[Pasted image 20220602211654.png]]

**in case of collision**
- Seperate chaining is when you have a collision you add another value to the same position worst case is O(n) if everything is put in the same
- linear probing is getting to the next empty spot to be inserted
- cuckoo hashing

# Graphs 

| Term                        | Definition                                               |
| --------------------------- | -------------------------------------------------------- |
| endpoints                   | the vertexes the edges are connecting                    |
| incident                    | the edges that are connected to a vertex                 |
| adjacent vertexes/neighbour | vertexes that are connected to each other                |
| degree                      | number of edges a vertex has                             |
| parallel edges              | when there are 2 edges that connect to the same vertexes |
| self loop                   | when it loops on itself                                  |
| simple                      | no parallel or self loops                                                         |

**directed graphs**

| Term           | Definition                                                            |
| -------------- | --------------------------------------------------------------------- |
| Tail           | where the edge goes to (the point of the edge)                        |
| Head           | where the edge starts                                                 |
| Out-degree     | is # of edges out of a vertex                                         |
| In-degree      | # of edges into a vertex                                              |
| Parallel edges | share tail and head (have to have the arrows pointed at the same way) |

## Implementation

### Adjacency List
Additionally each vertex keeps a sequence of edges incident on it. Edge objects keep reference to their position in the incidence sequence of its endpoints

```c
struct Node {
	*void value;
	*Node next;
}

struct vertex{
	void* value;
	Node* list_of_incident //a linked list of edges
}

struct edge{
	//not actual head and tails because it is not directed
	vertex* head;
	vertex* tail;
}
```

![[Pasted image 20220603124821.png]]
### Adjacency Matrix
A 2D array that stores the edges as such

![[Pasted image 20220603124846.png]]

## Graph Traversals
assume you are given the adjacency list representation

A systematic and structured way of visiting all the vertices and all the edges of a graph

### Depth First Search (DFS)
attempts to go as far into the tree as possible following a path, and backtracking when there are no more edges going down that path

if done correctly, it should return a tree representation of the graph

![[Depth-First-Search.gif]]

```python
def DFS(s):
    stack = [s]
    visited = set()
    # when current vertex is t then stop exploring
    while len(stack) > 0:
        # takes the top value of the stack and explores it
        current_vertex = stack.pop()

        # if it has already been explored then go to the next value in the stack
        if current_vertex in visited:
            continue
         
        visited.add(current_vertex)
        for edge in current_vertex.edges:
            stack.append(edge)

    return path if path[len(path) - 1] == t else None
```

### Breadth First Search (BFS)
Explores the graph through layers, explores each level and goes one deeper until they have all been exhausted. 

O(n + m)

![[Breadth-First-Search-Algorithm.gif]]

![[Pasted image 20220603130610.png]]

## Weighted Graphs

### Dijkstra's algorithm
**calculates the shortest path to every node from a starting node**

The base of the algorithm is that it gives every vertex a value on how much it "costs" to get there.

initially set every node to have a cost of infinite.
set the starting node as 0

it follows a path through the actual graph to decide where to go next and calculate how much it costs to get there. 

as you traverse, you increment the current weight the vertex has, and then add the new edge weight to see how much it takes to get to the NEW vertex

if the current weight is less than the new weight, then change the parent

![[Dijkstra_Animation.gif]]

![[Pasted image 20220602124026.png]]

**To calculate the actual smallest weight *OVERALL* then you use these algorithms**

### Smallest weight overall

#### Prim's algorithm

pick an arbitrary edge
then pick the smallest path to any vertex
if a vertex has already been encountered then there is no need to pick it

IT GOES DOWN A PATH OF VERTICIES AND DECIDES WHICH ONE IT SHOULD GO TO ***NEXT***

![[Pasted image 20220602124155.png]]

![[Prim-animation.gif]]

#### Kruskal's algorithm
always pick the smallest edge
keep adding edges untill all verticies are added to the MST
if there is an edge with the vertex already added down add it

IT PICKS THE SMALLEST EDGE WEIGHT REGARDLES OF WHERE THE ALGORITHM IS, IT DOESNT GO DOWN A PATH IT JUST KEEPS POPPING ANY EDGE THAT IS MINIMUM 

![[Pasted image 20220602124245.png]]
![[kruskal-animation.gif]]


# Minimum Spanning Trees
Minimum spanning trees are trees that have the least amount of edges possible

## Properties of an MST
- **Cut property**
	- if one single edge is removed from the MST then the tree must no longer be connected
	- **EXPLAINATION:** the minimum spanning tree should really only need to take 1 direct path to every node. so if one thing is removed from this path, then there is no path to other nodes
- **Cycle property**
	- if a tree has a cycle it is not a minimum spanning tree
	- **EXPLAINATION:** if there is a cycle this means there is more than 1 way to get to a certain node, and if this is true that means it doesnt take the most efficient route (doesnt use the least number of edges to get to the tree)

# Greedy Algorithm
A greedy algorithm constructs the solution in a greedy fashion, so after every element it processes, it makes some irrevocable choice (typically add or not add the processed element or something similar to that). 

If you build a data structure, you're likely not making any choices while processing the elements, instead delaying the choices and the construction of the solution until the very end of the algorithm.

That's indeed basically the case. A greedy algorithm makes irrevocable decisions while creating the output. If you're creating a binary search tree from the input and then using that, you aren't doing this (as you aren't making any decisions while processing the input) and I wouldn't consider that approach greedy.

when a solution updates is answers when it considers more data then it is not a greedy algorithm

This is not really a greedy algorithm, as you sort your input, then iterate through your whole input and perform a bunch of computations and updates to your towers before finally producing them.

A greedy solution makes decisions without much knowledge of the broader data, and so should iterate through the intervals and make a decision on whether or not to open a tower at each step. Greedy algorithms are also much simpler (for a problem like this).

to be greedy it would need to
- loop through all the input and would always need to make the best decision based on that input 
- those decisions cant be updated when you encouter new data

**Picks the largest**
**Picks the smallest weight**
**Picks best ratio**

# Divide and Conquer
1. Divide If it is a base case, solve directly, otherwise break up the problem into several parts. 
2. Recur/Delegate Recursively solve each part [each sub-problem]. 
3. Conquer Combine the solutions of each part into the overall solution

essentially to do it is to assume that the "recursion fairy" (the recursion fairy works the same as the inductive hypothesis, where you have to take a leap of faith and believe it works before you finish) will already give you exactly what you need. then you decide what to do with that.

so assume you are at the very last step of the algorithm, what do you need to do to return the FINAL answer. 

## Proving Correctness

**Inductive hypothesis:** what is the leap of faith you are taking? what are you assuming the "recursion fairy" returns

**Base Case:** the absolute last thing you are breaking the array down to. the smallest it gets

**Induction:** 
- assume the inductive hypothesis for an arbitrary number/size k, then prove it for number/size k + 1
- because of the inductive hypothesis, every thing the algorithm returns will be correct (e.g Splitting the array in half gives us two array of size at most k, so by IH those are sorted correctly)
- because you run the inductive hypothesis smaller ones and those have already worked if you were to apply those to the result you currently have to create something bigger it should still work?

## Master Theorum

![[Pasted image 20220604144348.png]]

$T(n) = aT(n/b) + O(1)$ 

$T(n) = T(n/2) + O(1)$ 

$a =$
$b =$
$f(n) =$

first calculate $n^{\log_b a}$ to find if it is > than f(n) = to f(n) or < than f(n), and thus find the case
$n^{\log_b a} =$


**MASTER THEORUM**

**Case 1:** $f(n) < n^{\log_b a}$                   AKA           $f(n) = O(n^{\log_b a - \epsilon})$ for $\epsilon > 0$
	$T(n) = \Theta(n^{\log_b a})$

**Case 2:** $f(n) = n^{\log_b a} \cdot \log^k n$        AKA          $f(n) = \Theta(n^{\log_b a} \cdot \log^k n)$ for $k  \ge 0$
	$T(n) = \Theta(n^{\log_b a} \cdot \log^{k + 1}(n))$

**Case 3:** $f(n) > n^{\log_b a}$                   AKA          $f(n) = \Omega(n^{\log_b a + \epsilon})$ and $a \cdot f(n/b) \le \delta f(n)$ for  $\epsilon > 0$ and $\delta < 1$ then
	$T(n) = \Theta(f(n))$

We have case -insert- 

which means:

$T(n) = O(n)$

