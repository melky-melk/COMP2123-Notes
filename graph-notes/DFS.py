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


def DFS(G):
	# set things up for DFS
	for u in G.vertices() do
		visited[u] ← False
		parent[u] ← None
	# visit vertices
	for u in G.vertices() do
		if not visited[u] then
			DFS_visit(u)
	
	return parent

def DFS_visit(u)
	visited[u] ← True
	# visit neighbors of u
	for v in G.incident(u) do
		if not visited[v] then
			parent[v] ← u
			DFS_visit(v)



def DFS(G):
	# set things up for DFS
	for u in G.vertices() do
		visited[u] ← False
		parent[u] ← None
	# visit vertices
	for u in G.vertices() do
		if not visited[u] then
			DFS_visit(u)
	
	return parent




# Using a Python dictionary to act as an adjacency list
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, '5')

        stack = [s]
        path = []
        if s == t:
            return path
        visited = set()
        untrusted_edges = 0

        # when current vertex is t then stop exploring
        while len(stack) > 0:
            # takes the top value of the stack and explores it
            current_vertex = stack.pop()

            # if it is the end vertex then simply return 
            if current_vertex == t:
                path.append(current_vertex)
                break

            # if it has already been explored then go to the next value in the stack
            if current_vertex in visited:
                continue

            visited.add(current_vertex)
            
            if (current_vertex.is_trusted == False): #add case where if the parent is untrusted add one (because there is a possibility that when the continue occurs it can go to )
                untrusted_edges += 1
                print("untrusted edge ", untrusted_edges  )

                # FIXME there is going to be some weird test case, where you need to go BEFORE the first untrusted as well and the number will be messed up maybe perform a check when the loop is over??? but thats O(n)^2??? idk maybe need to make recursive
                # this could work just change the condition??
                if untrusted_edges >= 2:
                    untrusted_edges = 0
                    
                    # goes to the next item needed before it can traverse the current vertex and add its own parts of the stack
                    continue 

            path.append(current_vertex)


            print("inside function")
            print("current: "+ str(current_vertex))
            
            for edge in current_vertex.edges:
                print("edge " + str(edge))
                if not edge in visited:
                    stack.append(edge)

            print("=======stack=======")
            for vertex in stack:
                print(vertex)

        return path 