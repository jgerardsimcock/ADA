import heapq

class PriorityQueue(object):
  """
  Priority Queue based on heap implementation, capable of inserting a new node
  with desired priority, updating the priority of an existing node
  and deleting arbitrary node while keeping invariants intact
  """

  def __init__(self, heap=[]):
    """
    if 'heap' is not empty, heapify it
    """

    heapq.heapify(heap)
    self.heap = heap
    self.entry_finder = dict({i[-1]: i for i in heap})
    self.REMOVED = '<remove_marker>'


  def insert(self, node, priority=0):

    """
    entry_finder is a bookkeeper of valid entries binded in heap. 
    If you change either, you change both
    """

    if node in self.entry_finder:
      self.delete(node)
    entry = [priority, node]
    self.entry_finder[node] = entry
    heapq.heappush(self.heap, entry)

  def delete(self,node):

    """
    Remove entry by marking it as 'removed' in heap and remove it from 'entry_finder'
    'pop()' method will delete the nodes
    """

    entry = self.entry_finder.pop(node)
    entry[-1] = self.REMOVED
    return entry[0]

  def pop(self):

    """
    If a node is marked 'REMOVED' it will not return.
    """

    while self.heap:

      priority, node = heapq.heappop(self.heap)
      if node is not self.REMOVED:
          del self.entry_finder[node]
          return priority, node 

    raise KeyError("pop from an empty priority queue")

def dijkstra(source, pq, edges):
  """
  Returns the shortest paths from the source to all other nodes.
  'edges': {tail: [(head, edge_dist), ]} contain all edges of the graph
  If undirected it contains both directions. 
  """

  size = len(pq.heap) + 1
  processed = [source]
  uncharted = set([i[1] for i in pq.heap])
  shortest_path = {}
  shortest_path[source] = 0
  while size > len(processed):
    min_dist, new_node = pq.pop()
    processed.append(new_node)
    uncharted.remove(new_node)
    shortest_path[new_node] = min_dist
    for head,edge_dist in edges[new_node]:
        if head in uncharted:
          old_dist = pq.delete(head)
          new_dist = min(old_dist, min_dist + edge_dist)
          pq.insert(head, new_dist) 

  return shortest_path

def test():

  BIG = 100000
  heap = [[2,2], [1,3], [BIG,4], [BIG, 5]]
  pq = PriorityQueue(heap)
  source = 1

  edges = {
           1: [(2,2), (3,3)], 
           2: [(1, 2), (3,2), (4,1)],
           3: [(1,1), (2,2), (4,1)],
           4: [(2,1), (3,1), (5,2)],
           5: [(4,2)]
           }

  return dijkstra(source, pq, edges)

def main():

  edges = {}
  heap = []
  source = 1

  BIG = 1000000
  goal = [7,37,59,82,99,115,133,165,188,197]

  with open('dijkstraData.txt') as file_in:

    for line in file_in:
      x = line.strip().split()
      node = int(x[0])
      edges[node] = [(int(i.split(',')[0]), int(i.split(',')[1]))
                      for i in x[1:]]

    for node in edges.keys():
        partial_edges = dict(edges[node])
        for i, dist_i in partial_edges.items():
            if i not in edges.keys():
              edges[i] = [(node,dist_i)]
            if (node, dist_i) not in edges[i]:
              edges[i].append((node,dist_i))

    source_edges = dict(edges[source])
    for node in range(2,201):
      if node in source_edges.keys():
        heap.append([source_edges[node], node])
      else:
        heap.append([BIG, node])

    pq = PriorityQueue(heap)
    shortest_path = dijkstra(source, pq, edges)
    out = [shortest_path[i] for i in goal]
    return out

if __name__ == '__main__':
    print main()








