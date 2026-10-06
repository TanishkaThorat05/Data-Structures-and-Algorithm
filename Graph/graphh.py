class Graph:
    def __init__(self,v):
        self.vertices=v
        self.AdjL=[[] for i in range(v)]
    def addEdge(self):
        e=int(input("Enter no of edges:"))

        for i in range(e):
            print(f"Enter edge {i+1}")
            u=int(input("Enter start vertex:"))
            v=int(input("Enter end vertex:"))
            self.AdjL[u].append(v)
            self.AdjL[v].append(u)
    def display(self):
        for i in range(self.vertices):
            print(i,"->",self.AdjL[i])

    def bfs(self,start):
        visited=[False]*self.vertices
        q=Queue()
        q.insert(start)
        visited[start]=True

        while q.front!=-1:
            current=q.delete()
            print(current)

            for vertex in self.AdjL[current]:
                if visited[vertex]==False:
                    visited[vertex]=True
                    q.insert(vertex)
  
class Queue:
    def __init__(self):
        self.front=-1
        self.rear=-1
        self.QT=[0]*5

    def insert(self,x):
        if self.rear==4:
            print("queue is full")
            return
        self.rear=self.rear+1
        self.QT[self.rear]=x

        if self.front==-1:
            self.front=0
    def delete(self):
        if self.front==-1:
            print("nothing to print")
            return
        else:
            y=self.QT[self.front]
        if self.front==self.rear:
            self.front=self.rear=-1
        else:
            self.front=self.front+1
        return y
    def display(self):
        if self.front==-1:
            print("nothing to print")
            return
        for i in range(self.front,self.rear+1):
            print(self.QT[i])

    
    
ob=Graph(3)
ob.addEdge()
ob.display()
start=int(input("Enter start vertex:"))
ob.bfs(start)