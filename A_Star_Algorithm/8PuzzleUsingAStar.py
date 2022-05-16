from typing import List
from copy import deepcopy

class Node:
    def __init__(self,matrix : List[List[int]], g_x : int,goal: List[List[int]]) -> None:
        self.matrix = matrix
        self.g_x = g_x
        self.h_x = 0
        self.f_x = 0
        self.goal = goal
        self.n = 3
        self.calculate_h_x()
        self.calculate_f_x()

    def locateZero(self):
        for i,row in enumerate(self.matrix):
            for j,ele in enumerate(row):
                if ele == 0:
                    return (i,j)
    
    def generateChildren(self):
        x,y = self.locateZero()
        possible = [
            (x+1,y),
            (x,y+1),
            (x-1,y),
            (x,y-1)
        ]
        children : List[Node] = []
        for i,j in possible:
            if i >= 0 and i < self.n and j >= 0 and j < self.n:
                child = deepcopy(self.matrix)
                child[x][y], child[i][j] = child[i][j], child[x][y]
                children.append(Node(child,self.g_x + 1,self.goal))
        return children
    
    def calculate_h_x(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.goal[i][j] != self.matrix[i][j]:
                    self.h_x += 1
        
    def calculate_f_x(self):
        self.f_x = self.g_x + self.h_x
    
    def printNode(self):
        print(f"g(x) = {self.g_x}")
        print(f"h(x) = {self.h_x}")
        print(f"f(x) = {self.f_x}")
        for i,row in enumerate(self.matrix):
            for j,ele in enumerate(row):
                print(ele,end=" ")
            print()
        print()

class Puzzle:
    def __init__(self) -> None:
        self.visited : List[Node] = []
        self.expanded : List[Node] = []
        self.n = 3
        self.initial = [[] for _ in range(self.n)]
        self.goal = [[] for _ in range(self.n)]
    
    def input(self, variable):
        print("Enter state.\n0 represents blank tile")
        for i in range(self.n):
            variable[i] = [int(j) for j in input().split(" ")]
    
    def solve(self):
        matrices= []
        print("Enter initial state")
        self.input(self.initial)
        print("Enter goal state")
        self.input(self.goal)
        print("\nSTART")
        current = Node(self.initial,0,self.goal)
        matrices.append(current.matrix)
        self.expanded.append(current)
        while True:
            current = self.expanded.pop(0)
            if current.h_x == 0:
                break
            current.printNode()
            for child in current.generateChildren():
                if child.matrix not in matrices:
                    matrices.append(child.matrix)
                    self.expanded.append(child)
            self.visited.append(current)
            self.expanded.sort(key=lambda x : x.f_x,reverse=False)
        current.printNode()


puzzle = Puzzle()
puzzle.solve()
