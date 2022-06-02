def Kruskal(G,c):
	sort E in increasing c-value
	answer ← [ ]
	comp ← make_sets(V)
	# for every pair of values inside the edges
	for (u,v) in E do
		# if the verticies do not make a cycle then add it
		if comp.find(u) != comp.find(v) then
			answer.append( (u,v) )
			comp.union(u, v)
	return answer

# unions are a data type that keeps track of the union and relationships between data points. it can combine 2 sets, but it cannot split them apart again