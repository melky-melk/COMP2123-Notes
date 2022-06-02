#takes a graph, all the edge weights and the starting vertex
def Dijkstra(G, w, s):
	# initialize algorithm by setting the values to be the same length as every vertex
	for v in V do
		#remember that the array D holds information about all the DISTANCES FROM S TO THE VERTEX, it isnt a typical array, in these lectures the pseudocode doesnt use indexes but the values themselves so its difficult to know it is more just a place to store all the distances. by setting it to infinity it ensures that the distance will get replaces by something smaller
		#it makes more sense if distances was a hashmap, with vertexes as the key and distances as the value. but in this case just assume that when you reference distances[v] you are accessing the v.distance because it functions like an attribute to v (because distances[value] is used later its vetter to think of it as a hashmap)
		distances[v] ← ∞
		path_tree[v] ← ∅ # storing the vertex used to access the current vertex (stores the vertex before)

	#the shortest path to itself is 0 so it starts at 0 and gets appended to
	distances[s] ← 0
	#use distance values as the key of the priority queue and the vertex as the value. 
	Q ← new priority queue for { (v, distances[v]) : v in V }
	
	# iteratively add vertices to S
	while Q is not empty do

		# removes the smallest distance of the priority queue
		smallest_vertex ← Q.remove_min()

		# goes through each of the edges inside the vertex
		for neighbor in G.neighbors(smallest_vertex) do

			# if the distance of the path to the smallest vertex + the weight of the edge to the next vertex (the neighbour being the next "level" down in depth) is smaller than the distance of just the neighbor
			if distances[smallest_vertex] + weight[smallest_vertex, neighbor] < distances[neighbor] then
				# update the smallest value to the neighbor to be the new value
				distances[neighbor] ← distances[smallest_vertex] + weight[smallest_vertex, neighbor]
				Q.update_priority(neighbor, distances[neighbor])
				# make put the smallest vertex into the path
				path_tree[neighbor] ← smallest_vertex
	
	# returns the distances from s to every vertex in the graph
	# and the smallest path tree
	return distances, path_tree

#at the end of the algorithm, the programmer will be able to know the smallest distance needed from s to any vertex in the graph
