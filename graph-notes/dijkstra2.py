from queue import PriorityQueue
import heapq as hq

def Dijkstra(G, weight, s):

	distances = {}
	for v in V do
		#it makes more sense if distances was a hashmap, with vertexes as the key and distances as the value. but in this case just assume that when you reference distances[v] you are accessing the v.distance because it functions like an attribute to v (because distances[value] is used later its vetter to think of it as a hashmap)
		distances[v] = float('inf')
		path_tree[v] = None # storing the vertex used to access the current vertex (stores the vertex before)

	#the shortest path to itgraph is 0 so it starts at 0 and gets appended to
	distances[s] = 0
	#use distance values as the key of the priority queue and the vertex as the value. 
	Q = PriorityQueue()
	
	for key, value in distances:

	new priority queue for { (v, distances[v]) : v in V }
	
	while not pq.empty():
		(dist, current_vertex) = pq.get()
		# self.visited.append(current_vertex)
		
		# visits all the neighbours the current edge is connected to 
		for neighbor in current_vertex.edges:
			new_cost = distances[smallest_vertex] + weight[smallest_vertex, neighbor]
			old_cost = distances[neighbor]
			# if the distance of the path to the smallest vertex + the weight of the edge to the next vertex (the neighbour being the next "level" down in depth) is smaller than the distance of just the neighbor
			if  new_cost < old_cost:
				# update the smallest value to the neighbor to be the new value
				distances[neighbor] = new_cost
				# change the old value
				Q.update_priority(neighbor, distances[neighbor])
				# make put the smallest vertex into the path
				path_tree[neighbor] = smallest_vertex
	
	# returns the distances from s to every vertex in the graph
	# and the smallest path tree
	return distances, path_tree

#at the end of the algorithm, the programmer will be able to know the smallest distance needed from s to any vertex in the graph
class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

	def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

	def dijkstra(self, start_vertex):
		# set all distances to be infinity 
		D = {v:float('inf') for v in range(self.v)}
		D[start_vertex] = 0

		pq = PriorityQueue()
		pq.put((0, start_vertex))
		visited = []

		while not pq.empty():
			(dist, current_vertex) = pq.get()
			visited.append(current_vertex)
			
			# visits all the neighbours the current edge is connected to 
			for neighbor in current_vertex.edges:
				if neighbor not in visited:
					# if the distance of the path to the smallest vertex + the weight of the edge to the next vertex (the neighbour being the next "level" down in depth) is smaller than the distance of just the neighbor
					new_cost = distances[smallest_vertex] + weight[smallest_vertex, neighbor]
					old_cost = distances[neighbor]
					if  new_cost < old_cost:
						# update the smallest value to the neighbor to be the new value
						distances[neighbor] = new_cost
						# change the old value
						Q.update_priority(neighbor, distances[neighbor])
						# make put the smallest vertex into the path
						path_tree[neighbor] = smallest_vertex

			for neighbor in range(self.v):
				if self.edges[current_vertex][neighbor] != -1:
					distance = self.edges[current_vertex][neighbor]
				
					if neighbor not in self.visited:
						old_cost = D[neighbor]
						new_cost = D[current_vertex] + distance
				
						if new_cost < old_cost:
							pq.put((new_cost, neighbor))
							D[neighbor] = new_cost
		return D


# given the graph
# given a dictionary with the all the weights of the edges between them. so given 2 vertexes it can return the edge
def dijkstra(G, weight, start_vertex):
	# set all distances to be infinity 
	distances = {v:float('inf') for v in range(self.v)}
	distances = {v:None for v in range(self.v)}
	distances[start_vertex] = 0

	pq = PriorityQueue()
	
	pq.put((0, start_vertex))
	visited = []

	while not pq.empty():
		(dist, current_vertex) = pq.get()
		visited.append(current_vertex)
		
		# visits all the neighbours the current edge is connected to 
		for neighbor in current_vertex.edges:
			if neighbor not in visited:
				# if the distance of the path to the smallest vertex + the weight of the edge to the next vertex (the neighbour being the next "level" down in depth) is smaller than the distance of just the neighbor
				new_cost = distances[current_vertex] + weight[current_vertex, neighbor]
				old_cost = distances[neighbor]
				if new_cost < old_cost:
					# update the smallest value to the neighbor to be the new value
					distances[neighbor] = new_cost
					# change the old value
					Q.put(new_cost, neighbor)
					# make put the smallest vertex into the path
					path_tree[neighbor] = current_vertex

	return distances, path_tree

