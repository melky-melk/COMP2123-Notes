ladef BFS(G,s):
	# set things up for BFS
	for u in G.vertices() do
		#again assume that accessing the verticies in the array is like the index that can access the boolean value
		seen[u] ← False
		parent[u] ← None

	#the vertex given has been seen
	seen[s] ← True
	layers ← []
	current ← [s]
	next ← []

	# process current layer
	while not current.is_empty() do
		#add to the layer 
		layers.append(current)
		
		# iterate over current layer
		for u in current do
			# for all the vertices connected 
			for v in G.incident(u) do
			
				if not seen[v] then
					next.append(v)
					seen[v] ← True
					parent[v] ← u
		# update current & next layers
		current ← next
		next ← []

	
	return layers, parent