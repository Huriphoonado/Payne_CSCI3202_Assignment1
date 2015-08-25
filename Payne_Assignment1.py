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

# Node class to be used within the binary tree
class Node(object):
	def __init__(self, key, leftChild, rightChild, parent):
		self.key = key
		self.leftChild = leftChild
		self.rightChild = rightChild
		self.parent = parent

class Binary_Tree(object):
	# Tree begins with only a root node
	# Implemented using a python dictionary with node key as the key
	# Root of binary tree has key of 0
	def __init__(self):
		self.binary_tree = {0: Node(0, None, None, None)}
	
	# Add a new node to the tree given a parent node and key value
	def add(self, key, parent):
		if parent in self.binary_tree:
			# If left node is empty - make that the child node
			if self.binary_tree[parent].leftChild == None:
				self.binary_tree[parent].leftChild = key
				self.binary_tree[key] = Node(key, None, None, parent)
			# If right node is empty - make that the child node
			elif self.binary_tree[parent].rightChild == None:
				self.binary_tree[parent].rightChild = key
				self.binary_tree[key] = Node(key, None, None, parent)
			else:
				print "Parent has two childen, node not added."
		else:
			print "Parent not found."

	# Removes a node from the tree and makes sure the node is no longer listed as a child
	def delete(self, key):
		if key in self.binary_tree:
			if self.binary_tree[key].leftChild != None or self.binary_tree[key].rightChild != None:
				print("Node not deleted, has children.")
			else:
				current_parent = self.binary_tree[key].parent
				
				# first set the correct node of the parent to None
				if self.binary_tree[current_parent].leftChild == key:
					self.binary_tree[current_parent].leftChild = None
				else:
					self.binary_tree[current_parent].rightChild = None

				# then remove the node from the binary tree
				del self.binary_tree[key]
		else:
			print "Node not found."

	# Prints the entire tree starting with the root node
	# pre_order traversal implemented with recursion
	def printTree(self):
		# helper function that can be called with the key of the current node
		def printTreeHelper(key):
			# first print center node
			print self.binary_tree[key].key,
			if self.binary_tree[key].leftChild != None:
				# then call with left node
				printTreeHelper(self.binary_tree[key].leftChild)
			if self.binary_tree[key].rightChild != None:
				# then call with right node
				printTreeHelper(self.binary_tree[key].rightChild)

		# Call the print tree function with the root node
		print "Nodes:",
		printTreeHelper(0)
		print ""

# -------------------------------------------------------------

# 4. Implement an unweighted graph using a dictionary

# graph consists of a dictionary of key-value pairs
# 	keys are integers representing vertices
# 	values are lists representing adjacent vertices
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

# -------------------------------------------------------------

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

# # Since queue is FIFO - values should print in reverse order of being added
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

# Since stack is FIFO - values should print in order of being added
print "Popped Values:", my_stack.pop(), my_stack.pop(), my_stack.pop(), my_stack.pop(), my_stack.pop(), 
print my_stack.pop(), my_stack.pop(), my_stack.pop(), my_stack.pop(), my_stack.pop()

# -------------------------------------------------------------

# 3. Binary Tree

# Make a new binary tree
myTree = Binary_Tree()

# Add nodes to the tree (left to right and then down)
myTree.add(1, 0)
myTree.add(2, 0)
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