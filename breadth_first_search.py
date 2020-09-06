from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v): # want to add the edge from u to v
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.graph[v].remove(u) # want the nodes without executing edge in our list as well
    
    def use(self, v):
        print(v)


    def breadth_first_search(self, start):
        visited = [False] * len(self.graph) # want to create the visited array
        print(self.graph)
        queue = [start]
        visited[start] = True # had to put in the first element in queue manually so the while loop is working properly

        while len(queue) > 0:
            start = queue.pop(0) # pop the first element and use it as new start element
            self.use(start)
            for i in self.graph[start]:
                if visited[i] == True: # if the node is already visited we dont have to append that
                    continue
                queue.append(i)
                visited[i] = True


g = Graph()
g.add_edge(0,2) # edge from 0 to 2
g.add_edge(0,4)
g.add_edge(2,4)
g.add_edge(1,3)
g.add_edge(4,1)
g.add_edge(4,0)
g.add_edge(4,2)
print('Starting breadth first search')
g.breadth_first_search(0)