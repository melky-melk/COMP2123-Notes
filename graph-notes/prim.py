def prim(G, c):
	u ← arbitrary vertex in V
	S ← { u }
	T ← ∅
	while len(S) < len(V) do
		# in every iteration, you are picking the edge that has to be in the minimum spanning tree??
		(u, v) ← min cost edge s.t. u in S and v not in S
		add (u, v) to T
		add v to S

	return T

def prim(G, c) {
	for v in V do
		d[v] ← ∞
		spanning_tree[v] ← None

	u ← arbitrary vertex in V
	d[u] ← 0
	#again storing the vertexes and their distances
	Q ← new PQ with items { (v, d[v]) for v in V }
	# s being the final sprawling tree
	S ← None
	
	while Q is not empty do
		# again pop the current minimum element (the one with the lowest distance) from 
		u ← delete min element from Q
		add u to S

		# go through all edges u has
		for (u, v) incident to u do
			#if the vertex next to u is not in the set and the edge weight is lower than the current edge weight
			if v not in S and ce < d[v] then
				spanning_tree[v] ← u
				decrease priority d[v] to ce
	return spanning_tree

# 1:13:20 in week8 lecture