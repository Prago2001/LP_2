class Dijkstra:
    def __init__(self) -> None:
        self.vertices = int(input("Enter number of vertices: "))
        self.graph = [[float('inf')]*self.vertices for _ in range(self.vertices)]

        self.edges = int(input("Enter number of edges: "))
        print("Start\tEnd\tDistance")
        for inp in range(self.edges):
            v1,v2,e = input().split(" ")
            v1 = int(v1)
            v2 = int(v2)
            e = int(e)
            self.graph[v1-1][v2-1] = e
            self.graph[v2 - 1][v1- 1] = e
        
        for i in range(self.vertices):
            self.graph[i][i] = 0
    
    def printMatrix(self):
        print("\t",end="")
        for i in range(self.vertices):
            print(i+1,end="\t")
        print()
        for i,row in enumerate(self.graph):
            print(i+1,end="\t")
            for ele in row:
                print(ele,end="\t")
            print()
    
    def solve(self):
        source = int(input("Enter starting node:"))
        visited = set()
        distances = [float('inf')] * self.vertices
        distances[source - 1] = 0

        while True:
            minDist = float('inf')
            minId = -1
            for i,dist in enumerate(distances):
                if dist < minDist and i not in visited:
                    minDist = dist
                    minId = i
            
            if minId == -1:
                break

            for i,distance in enumerate(self.graph[minId]):
                if distances[i] > minDist + distance:
                    distances[i] = minDist + distance
            visited.add(minId)
        
        print(f"Distances from source {source}:")
        for i,distance in enumerate(distances):
            print(f"Distance to {i+1}: {distance}")



solver = Dijkstra()
solver.printMatrix()
solver.solve()