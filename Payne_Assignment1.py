# Willie Payne
# CSCI 3202 Assignment 1

from collections import deque

# Data structures including Queue, Stack, Binary Tree, Graph

# 1. Implement a queue that only takes in integers

# Queue without predetermined size that takes in integers
class Integer_Queue(object):
    # Initialized with the double-ended queue from the Collections module
    def __init__(self):
        self.queue = deque()

    # Add integers to the left of the queue
    def add_int(self, item):
    	if type(item) == int:
    		self.queue.appendleft(item)
    
    # Remove the integers from the right of the queue
    # First In First Out (FIFO)
    def dequeue(self):
    	return self.queue.pop()

# -------------------------------------------------------------

# 2. Implement a stack using the list class

class Stack(object):
	# Initialize the stack using an empty list
	def __init__(self):
		self.stack = []

	# add a new item to the stack - gets added to the right
	def push(self, item):
		self.stack.append(item)

	# returns and removes the last item in the list (lifo)
	# Last In First Out (LIFO)
	def pop(self):
		return self.stack.pop()

	# returns the length of the stack
	def checkSize(self):
		return len(self.stack)

# -------------------------------------------------------------

# 3. Implement a Binary Tree

class Node(object):
	def __init__(self, key, parent):
		self.key = key # Integer key value
		self.leftChild = None # Node left child
		self.rightChild = None # Node left child
		self.parent = parent # Node parent added to

class Binary_Tree(object):
	# Initialize the tree with a root node of key value 0
	def __init__(self):
		self.rootNode = Node(0, None)

	# Adds a node to the tree
	# 	1. Searches through the tree to find the parent node
	# 	2. If parent found, node is inputted into avaible child spot - left then right
	#	3. New child is initialized with given key and newfound parent
	def add(self, value, parentValue):
		# gets set to 1 if the parent node is found anywhere
		# within the recursive function calls
		global nodeFound
		nodeFound = 0
		
		# Helper function called with the root node of the tree
		def addHelper(value, parentValue, parentNode):
			global nodeFound
			if parentNode.key == parentValue: # we have found a match
				if parentNode.leftChild == None:
					parentNode.leftChild = Node(value, parentNode)
					nodeFound = 1
					return
				elif parentNode.rightChild == None:
					parentNode.rightChild = Node(value, parentNode)
					nodeFound = 1
					return
				else:
					print "Parent has two childen, node not added."
					nodeFound = 1
					return
			else: # search through the rest of the tree
				if parentNode.leftChild != None:
					addHelper(value, parentValue, parentNode.leftChild)
				if parentNode.rightChild != None:
					addHelper(value, parentValue, parentNode.rightChild)
				elif parentNode.leftChild == None and parentNode.rightChild == None:
					return
		
		# Call the helper function
		addHelper(value, parentValue, self.rootNode)
		if nodeFound == 0:
			print "Parent not found"

	# Remove a node from the tree
	# 	1. Searches through the tree to find the given node
	# 	2. If node found, make sure it has no children
	# 	3. Node is removed by setting its parent's child parameter back to None
	def delete(self, value):
		global nodeFound
		nodeFound = 0

		def deleteHelper(value, currentNode):
			global nodeFound
			if currentNode.key == value: # we found a match
				# correct node has children -> stop
				if currentNode.leftChild != None or currentNode.rightChild != None:
					nodeFound = 1
					print "Node not deleted, has children."
					return
				else: # Correct node has no children -> delete
					nodeFound = 1
					if currentNode.parent.leftChild.key == currentNode.key:
						currentNode.parent.leftChild = None
						return
					else:
						currentNode.parent.rightChild = None
						return
			else: # look through the rest of the tree
				if currentNode.leftChild != None:
					deleteHelper(value, currentNode.leftChild)
				if currentNode.rightChild != None:
					deleteHelper(value, currentNode.rightChild)
				elif currentNode.leftChild == None and currentNode.rightChild == None:
					return

		deleteHelper(value, self.rootNode)
		if nodeFound == 0:
			print "Parent not found"

	# Print the entire tree via pre-order traversal
	def printTree(self):
		# helper function that can be called with the root node
		def printTreeHelper(currentNode):
			# first print center node
			print currentNode.key,
			if currentNode.leftChild != None: # then call with left node
				printTreeHelper(currentNode.leftChild)
			if currentNode.rightChild != None: # then call with right node
				printTreeHelper(currentNode.rightChild)

		# Call the print tree function with the root node
		print "Nodes:",
		printTreeHelper(self.rootNode)
		print ""

# -------------------------------------------------------------

# 4. Implement an unweighted graph using a dictionary

# Graph consists of a dictionary of key-value pairs
# 	Keys are integers representing vertices
# 	Values are lists representing adjacent vertices
class Graph(object):
	def __init__(self):
		self.vertices = dict()

	# Adds a new integer vertex to the list
	def addVertex(self, vertex):
		if vertex in self.vertices:
			print("Vertex already exists.")
		else:
			self.vertices[vertex] = []

	# Adds an edge between two existing vertices
	# Not limited - vertices can connect to themselves
	# Not limited - vertices can have multiple edges with eachother
	def addEdge(self, vertex1, vertex2):
		# if both vertices exist then each should hold the other in its edges list
		if vertex1 in self.vertices and vertex2 in self.vertices:
			self.vertices[vertex1].append(vertex2)
			self.vertices[vertex2].append(vertex1)
		else:
			print "One or more vertices not found."

	def findVertex(self, vertex):
		if vertex in self.vertices:
			print_edges = (str(v) for v in self.vertices[vertex])
			print "Vertex:", vertex, "Adjacent Vertices:", ", ".join(print_edges)
		else:
			print "Vertex not found."


# -------------------------------------------------------------
# -------------------------------------------------------------

# Tests

# 1. Queue

# Make a new queue
my_queue = Integer_Queue()

# Add values to the queue
my_queue.add_int(1)
my_queue.add_int(2)
my_queue.add_int(3)
my_queue.add_int(4)
my_queue.add_int(5)
my_queue.add_int(6)
my_queue.add_int(7)
my_queue.add_int(8)
my_queue.add_int(9)
my_queue.add_int(10)

# # Since queue is FIFO - values should print in order of being added
print "Dequeued Values:",
print my_queue.dequeue(), my_queue.dequeue(), my_queue.dequeue(), my_queue.dequeue(), 
print my_queue.dequeue(), my_queue.dequeue(), my_queue.dequeue(), my_queue.dequeue(),
print my_queue.dequeue(), my_queue.dequeue()

# -------------------------------------------------------------

# 2. Stack

# Make a new stack
my_stack = Stack()

# Add values to the stack
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
my_stack.push(6)
my_stack.push(7)
my_stack.push(8)
my_stack.push(9)
my_stack.push(10)

# Size of stack should be 10 
print "Stack Size:", my_stack.checkSize()

# Since stack is LIFO - values should print in reverse order of being added
print "Popped Values:", my_stack.pop(), my_stack.pop(), my_stack.pop(), my_stack.pop(), my_stack.pop(), 
print my_stack.pop(), my_stack.pop(), my_stack.pop(), my_stack.pop(), my_stack.pop()

# -------------------------------------------------------------

# 3. Binary Tree

# Make a new binary tree
myTree = Binary_Tree()

# Add nodes to the tree (left to right and then down)
myTree.add(1, 0)
myTree.add(2, 0)
myTree.add(3, 0) # should print an error since root node already has two children
myTree.add(3, 1)
myTree.add(4, 1)
myTree.add(5, 2)
myTree.add(6, 2)
myTree.add(7, 3)
myTree.add(8, 3)
myTree.add(9, 4)
myTree.add(10, 4)
myTree.add(19, 11) # should print an error since 11 does not exist
myTree.printTree()

# Remove nodes
myTree.delete(7) # removes leftmost node on the bottom
myTree.delete(9) # removes second-to-right most node on bottom
myTree.delete(4) # should return an error since node has a child
myTree.printTree()

# -------------------------------------------------------------

# 4. Graph

# Initialize a graph
myGraph = Graph()

# Add vertices to the graph
myGraph.addVertex(1)
myGraph.addVertex(2)
myGraph.addVertex(3)
myGraph.addVertex(4)
myGraph.addVertex(5)
myGraph.addVertex(6)
myGraph.addVertex(7)
myGraph.addVertex(8)
myGraph.addVertex(9)
myGraph.addVertex(10)

# Add edges between vertices
myGraph.addEdge(1, 2)
myGraph.addEdge(1, 3)
myGraph.addEdge(1, 4)
myGraph.addEdge(1, 5)
myGraph.addEdge(1, 6)
myGraph.addEdge(1, 7)
myGraph.addEdge(1, 8)
myGraph.addEdge(1, 9)
myGraph.addEdge(2, 4)
myGraph.addEdge(2, 6)
myGraph.addEdge(2, 8)
myGraph.addEdge(9, 11) # should print error since 11 does not exist

# Print vertices and edges
myGraph.findVertex(1) # should have 8 edges
myGraph.findVertex(2) # should have 4 edges
myGraph.findVertex(3) # should have 1 edge
myGraph.findVertex(4) # should have 2 edges
myGraph.findVertex(10) # should have 0 edges