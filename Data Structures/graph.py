from collections import deque
class Graph:
    def __init__(self):
        self.graph={}
        self.adj_matrix=[]
    def add_node(self,v):
        if v in self.graph:
            print(v,"is already present in graph")
        else:
            self.graph[int(v)]=[]
    def add_edge(self,v1,v2):
        if int(v1) not in self.graph:
            print(v1,"is not present in the graph")
        elif int(v2) not in self.graph:
            print(v2,"is not present in the graph")
        else:
            self.graph[int(v1)].append(int(v2))
    def delete_node(self,v):
        if v not in self.graph:
            print(v,"is not present in the graph")
        else:
            self.graph.pop(v)
            for i in self.graph:
                list1=self.graph[i]
                if v in list1:
                    list1.remove(v)
    def adjacency_mat(self):
        n = len(self.graph)
        self.adj_matrix = [[0] * n for i in range(n)]

        index = {node: index for index, node in enumerate(self.graph.keys())}
        print('nodes:',*index.keys())
        for node, neighbors in self.graph.items():
            i = index[node]
            for neighbor in neighbors:
                j = index[neighbor]
                self.adj_matrix[i][j] = 1


        for row in self.adj_matrix:
            print(row)
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)

                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return result
    def dfs(self,vertex):
        visited=set()
        stack=[vertex]
        result=[]
        while stack:
            vertex=stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        stack.append(neighbor)
        return result
    def cycle(self,vertex):
        visited = set()
        stack = [vertex]
        result = []
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                for neighbor in self.graph[vertex]:
                    if self.adj_matrix[vertex][neighbor]==1 and neighbor not in visited:
                        stack.append(neighbor)
                    elif self.adj_matrix[vertex][neighbor]==1 and neighbor in visited:
                        result=['cycle']
        return result


    """def connected(self):
        ans=[]
        for i in self.graph:
            if ans:
                if len(self.graph[i])<0:
                    ans=False
            else:
                pass
        return ans"""
obj=Graph()
while True:
    lst=list(map(str,input().split()))
    if lst[0]=='null':
        break
    elif len(lst)==1:
        obj.add_node(lst[0])
    elif len(lst)==2:
        obj.add_edge(lst[0],lst[1])
#obj.adjacency_mat()
"""print(obj.graph)"""
#print(obj.bfs(2))
#print(obj.bfs('2'))
print(obj.cycle(list(obj.graph.keys())[0]))
"""if obj.connected():
    print('connected')
else:
    print('un connected')"""
#print(obj.bfs('2'))
#print(obj.dfs('2'))
print(obj.graph)
