import queue
from collections import defaultdict


class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        G = defaultdict(list)
        for i, j in enumerate(graph):
            G[i].extend(j)

        Stack = queue.LifoQueue()
        Visited = set()
        Colour = {}

        v = min(G.keys())

        Stack.put(v)
        Visited.add(v)
        Colour[v] = 1

        while not Stack.empty():
            cur = Stack.get()
            for neigh in G[cur]:
                if neigh not in Visited:
                    Colour[neigh] = Colour[cur] * -1
                    Visited.add(neigh)
                    Stack.put(neigh)
                elif Colour[neigh] == Colour[cur]:
                    return False
                else:
                    pass
        return len(Colour.keys()) == len(G.keys())


g = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
# g = [[1,3], [0,2], [1,3], [0,2]]
# g = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
g = [[4],[],[4],[4],[0,2,3]]
s = Solution().isBipartite(g)
print(s)
