**Problem 2.**
An undirected graph G = (V, E) is said to be bipartite if its vertex set V can be partitioned into two sets A and B such that E ⊆ A × B. 

Design an O(n + m) algorithm to test if a given input graph is bipartite using the following guide: 

Suppose we run BFS from some vertex s ∈ V and obtain layers L1, . . . , Lk . Let (u, v) be some edge in E. Show that if u ∈ Li and v ∈ Lj then |i − j| ≤ 1. 

**a) Suppose we run BFS on G. Show that if there is an edge (u, v) such that u and v belong to the same layer then the graph is not bipartite.** 

meaning that the vertexes can be divided in such a way that if you were to times them together they would all have a connection to the other?

if u is in one layer, then the v must be in a different layer. it cannot be in the same later, it can be in a lower or higher layer. by the absolute difference

the a vertex in the A set, will not connect to another vertex in the A set, by how the cartesian products of the vertexes' work. it would only connect to values inside B

meaning that there would have to be at least 2 layers, and the layers in teh first one MUST connext to a different layer in the graph.  

**b) Suppose we run BFS on G. Show that if there is an edge (u, v) such that u and v belong to the same layer then the graph is not bipartite**

meaning that there would have to be at least 2 layers, and the layers in teh first one MUST connext to a different layer in the graph.  

if its in a different layer, then it wouldnt work as a cartesian product of the vertexes

**c) Suppose G is connected and we run BFS. Show that if there are no intra-layer edges then the graph is bipartite.** 

if there are no intra connected edges that would mean every edge would have to extend to a different later

d) Put together all the above to design an O(n + m) time algorithm for testing bipartiness.

run BFS on the graph, check for intra connected edges, if tehre are none then it is bipartite

**Problem 3.** Give an O(n) time algorithm to detect whether a given undirected graph contains a cycle. If the answer is yes, the algorithm should produce a cycle. (Assume adjacency list representation.)

in the visited list there should be a DFS, if the path goes down to a vertex already visited then it should stop and return the path it was traveling down? 

**Problem 4.** Let G = (V, E) be an n vertex graph. Let s and t be two vertices. Argue that if dist(s, t) > n/2 then there there exists a vertex u != s, t such that every path from s to t goes through u.

**Problem 8**. Let T be a rooted tree. For each vertex u ∈ T we use Tu to denote the subtree of T made up by u and all its descendants. Assume each vertex u ∈ T has a value A[u] associated with it. Let B[u] = min{A[v] : v ∈ Tu}. Design an O(n) time algorithm that given A, computes B.

B[u] is the minimum A value in the subtree. 

the base case is the leaves of the node that have no children in which B[u] would just be A[u]

then to find all the ones above you would need to compare all the children the parent has and see which one is minimum

the correctness is through induction

any traversal is fine as long as the children are processed first