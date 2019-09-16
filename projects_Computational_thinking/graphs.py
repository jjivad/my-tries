# -*- coding: utf-8 -*-
"""
Created on Wed May  1 20:38:53 2019

@author: VIJ Global
"""

class node(object):
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + ' -> ' + self.dest.getName() 
class diagraph(object):
    #edges is a dict mapping each node to a list of its children
    def __init__(self):
        self.edges = {}
    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError ('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, name):
        return self.edges[node]
    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)
    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + ' -> ' + dest.getName() + ' \n'
        return result[:-1] #omit final newline
    
class graph(diagraph):
    def addEdge(self, edge):
        diagraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        diagraph.addEdge(self, rev)
        
def buildCityGraph(graphType):
    g = graphType()
    for name in ('Boston', 'Providence', 'New York', 'Chicago', 'Denver', 'Phoenix', 'Los Angeles'): #create 7 node
        g.addNode(node(name))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    return g
    
#print(buildCityGraph(diagraph))
print(buildCityGraph(graph))

def printPath(path):
    # assumes path is a list of nodess
    result = ''
    for i in range (len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + ' -> '
    return result

def DFS(graph, start, end, path, shortest, toPrint = True): #depth-first search algorithm
    #assumes graph is a digraph, start and end are node, path and shotest are lists of nodes
    #return a shortest path from start to end in graph
    path = path + [start]
    
    if toPrint:
        print('Current DFS path: ', printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest, toPrint)
                if newPath != None:
                    shortest = newPath
        elif toPrint:
            print ('Already visited ', node)
    return shortest

def shortestPath(graph, start, end, toPrint = False):
    #assumes grapgh is a digraph, start and end are nodes
    #returns a shortest path from start to end in graph
    return DFS(graph, start, end, [], None)

def testFSP(source, destination):
    g = buildCityGraph(diagraph)
    sp = shortestPath (g, g.getNode(source), g.getNode(destination), toPrint = False)
    if sp != None:
        print('')
        print('Shortest path form ', source, ' to ', destination, ' is ', printPath(sp))
    else:
        print('')
        print('There is no path from ', source, ' to ', destination)

#testSP is test shortest path

def BFS(graph, start, end, toPrint = False):  #breadth-first search algorithm
    #assumes graph is a digraph, start and end are nodes
    #returns a shortes path from start to end in graph
    initPath = [start]
    pathQueue = [initPath]
    if toPrint:
        print('Current BFS path: ', printPath(pathQueue))
    while len(pathQueue) != 0:
        #get and remove oldest element in pathQueue
        tmpPath = pathQueue.pop(0)
        print('Current BFS path: ', printPath(tmpPath))
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)
    return None

def shortestPathBFS(graph, start, end, toPrint = False):
    #assumes graph is a digraph, end and start are nodes
    #returns a shotest path from start to end in graph
    return BFS(graph, start, end, toPrint)

def testBSP(source, destination):
    g = buildCityGraph(diagraph)
    sp = shortestPathBFS (g, g.getNode(source), g.getNode(destination), toPrint = True)
    if sp != None:
        print('')
        print('Shortest path form ', source, ' to ', destination, ' is ', printPath(sp))
    else:
        print('')
        print('There is no path from ', source, ' to ', destination)

#testFSP('Chicago', 'Boston')
testFSP('Boston', 'Phoenix')
#testBSP('Chicago', 'Boston')
testBSP('Boston', 'Phoenix')
#assert False
        
    
   