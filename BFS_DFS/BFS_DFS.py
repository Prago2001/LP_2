from collections import deque
from typing import Deque, List

class Graph:
    def __init__(self) -> None:
        self.n = int(input("Enter number of nodes"))
        self.nodes = {i+1 : [] for i in range(self.n)}
    
    def addEdge(self,start:int,end:int):
        self.nodes[start].append(end)
        self.nodes[end].append(start)
    
    def printGraph(self):
        for node, list in self.nodes.items():
            print(f"{node} -> ",end="")
            for vertex in list:
                print(vertex,end=" ")
            print()
    
    def dfsHelper(self,current : int,visited : List[bool]):
        print(current,end= " ")
        visited[current] = True
        for adjacentNode in self.nodes[current]:
            if visited[adjacentNode] == False:
                self.dfsHelper(adjacentNode,visited)
    def dfs(self,start : int):
        visited = [False] * (self.n + 1)
        print(f"DFS from {start}: ",end="")
        self.dfsHelper(start,visited)
        print()
    
    def bfs(self,start:int):
        queue = deque()
        visited = [False] * (self.n + 1)
        print(f"BFS from {start}: ",end="")
        queue.append(start)
        visited[start] = True
        self.bfsHelper(queue,visited)
        print()

    def bfsHelper(self,queue : Deque,visited: List[bool]):
        if len(queue) == 0:
            return
        current = queue.popleft()
        print(current,end=" ")
        
        for adjacentNode in self.nodes[current]:
            if visited[adjacentNode] == False:
                queue.append(adjacentNode)
                visited[adjacentNode] = True
        self.bfsHelper(queue,visited)

g = Graph()
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(5,2)
g.addEdge(5,3)
g.addEdge(5,4)
g.printGraph()
g.dfs(3)
g.bfs(1)