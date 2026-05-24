#GRAPH
import sys
class Graphs:
    def __init__(self):
      self.nodes=[]
      self.graphs=[]
      self.nodeCount=0

    def addNode(self,v):
      if v in self.nodes:
        print(v,"node already exist")
      else:
        self.nodeCount+=1
        self.nodes.append(v)
        for  x in self.graphs:
          x.append(0)
        temp=[]
        for x in range(self.nodeCount):
          temp.append(0) #temp[]=0
        self.graphs.append(temp)
        print(v," is added")



    def addEdge_Undirected_Unweighted(self,v1,v2):
      if v1 not in self.nodes:
          print(v1,"node not exist")
          return
      if v2 not in self.nodes:
          print(v2,"node not exist")
          return
      index1=self.nodes.index(v1)
      index2=self.nodes.index(v2)
      self.graphs[index1][index2]=1
      self.graphs[index2][index1]=1


    def addEdge_Undirected_weighted(self):
       if v1 not in self.nodes:
        print(v1,"node not exist")
        return
       if v2 not in self.nodes:
        print(v2,"node not exist")
        return
        index1=self.nodes.index(v1)
        index2=self.nodes.index(v2)
        self.graphs[index1][index2]=weight
        self.graphs[index2][index1]=weight


    def addEdge_directed_weighted(self):
        if v1 not in self.nodes:
          print(v1,"node not exist")
          return
        if v2 not in self.nodes:
          print(v2,"node not exist")
          return
        index1=self.nodes.index(v1)
        index2=self.nodes.index(v2)
        self.graphs[index1][index2]=weight
    


    def printGraph(self):
      print(*self.nodes)
      for i in range(self.nodeCount):
        for j in range(self.nodeCount):
          print(self.graphs[i][j],end=" ")
        print("")
    def deletGraph(self,v): 
      if v not in self.nodes:
        print(v,"not present")
      else:
        self.nodeCount-=1
        index1=self.nodes.index(v)
        self.nodes.pop(index1)
        self.graph.pop(index1)
        for x in self.graph:
          x.pop(index1)
          print(v, "is deleted")

if __name__=="__main__":
  obj=Graphs()
  while True:
    print("\n1. (insertion) add a node using adjacency matrix representation");
    print("2. (insertion) add an edge using adjacency matrix representation");
    print("3. (insertion)add a edge undirected weighted graph");
    print("4. (insertion) add a edge directed weighted graph");
    print("5. print graph");
    print("6. delet operation");
    print("7. exit");
    n=int(input("enter any choice: "))
    if n==1:
      v=input("enter vertex")
      obj.addNode(v)
    elif n==2:
      v1=input("enter first vertex")
      v2=input("enter second vertex")
      obj.addEdge_Undirected_Unweighted(v1,v2)

    elif n==3:
      v1= input("enter first vertex")
      v2= input("enter second vertex")
      weight=int(input("enter weight"))
      obj.addEdge_Undirected_weighted()
    elif n==4:
      v1= input("enter first vertex")
      v2= input("enter second vertex")
      weight=int(input("enter weight"))
      obj.addEdge_directed_weighted()
    elif n==5:
      obj.printGraph()
    elif n==6:
      obj.deletGraph()
    elif n==0:
      sys.exit(0)
    else:
      print("invalid choice")