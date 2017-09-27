import networkx as nx

g = nx.Graph()
for i in range(2, 101):
  k = 2
  while i * k <= 100:
    g.add_edge(i, i * k)
    k += 1

longest = []


def dfs(used, longest):
  if len(used) > len(longest):
    del longest[:]
    longest.extend(used)
    print(longest, len(longest))

  used_set = set(used)
  edges = g.edges(used[-1])
  for edge in edges:
    n_val = edge[1]
    if n_val not in used_set:
      used.append(edge[1])
      dfs(used, longest)
      used.pop()

removable = list()
for i in range(1,101):
  if i not in g:
    continue
  edges = g.edges(i)
  if len(edges) == 2:
    removable.append(i)

print()
print(len(g))
print(len(removable))
# start = 93
# print(start)
# dfs([93], [])
