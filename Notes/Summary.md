# Trees
## Sorting of verticies




# Greedy Algorithm

SOMETHING IS A GREEDY ALGORITHM IF AND ONLY IF

**Picks the largest**
**Picks the smallest weight**
**Picks best ratio**


# Minimum Spanning Trees
Minimum spanning trees are trees that have the least amount of edges possible

## Properties of an MST
- **Cut property**
	- if one single edge is removed from the MST then the tree must no longer be connected
	- **EXPLAINATION:** the minimum spanning tree should really only need to take 1 direct path to every node. so if one thing is removed from this path, then there is no path to other nodes
- **Cycle property**
	- if a tree has a cycle it is not a minimum spanning tree
	- **EXPLAINATION:** if there is a cycle this means there is more than 1 way to get to a certain node, and if this is true that means it doesnt take the most efficient route (doesnt use the least number of edges to get to the tree)


## Weighted Minimum/Maximum Spanning Trees

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
# Divide and Conquer

## Master Theorum

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

