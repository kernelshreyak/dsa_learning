#Implementation of generic tree in Python

import pptree

class TreeNode(object):
    "Node of a Tree"
    def __init__(self, name='root', children=None,parent=None):
        self.name = name
        self.parent=parent
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)

    def __repr__(self):
        return self.name

    def is_root(self):
        if self.parent is None:
            return True
        else:
            return False
    def is_leaf(self):
        if len(self.children) == 0:
            return True
        else:
            return False

    def depth(self):    # Depth of current node
        if self.is_root():
            return 0
        else:
            return 1 + self.parent.depth()

    def add_child(self, node):
        node.parent=self
        assert isinstance(node, TreeNode)
        self.children.append(node)

    def disp(self):
        pptree.print_tree(self,'children','name')



class Tree:
    """
    Tree implemenation as a collection of TreeNode objects
    """
    def __init__(self):
       self.root=None
       self.height=0
       self.nodes=[]

    def insert(self,node,parent=None):   # Insert a node into tree
        if parent is not None:
            parent.add_child(node)
        else:
            if self.root is None:
                self.root=node
        self.nodes.append(node)

    def search(self,data):  # Search and return index of Node in Tree
        index=-1
        for N in self.nodes:
            index+=1
            if N.name == data:
                break
        if index == len(self.nodes)-1:
            return -1  #node not found
        else:
            return index

    def getNode(self,id):
        return self.nodes[id]

    def root(self):
        return self.root
    
    # Returns depth of a node
    def depth(self,p: TreeNode):
        return p.depth()

    def height(self):
        return 100

#----------------------------------------------------------------------
# Binary TreeNode Implementation
class BinaryTreeNode(Tree):
    def __init__(self, name='root', children=None,parent=None):
       pass
#----------------------------------------------------------------------

tree = Tree()
node1 = TreeNode('root')
node2 = TreeNode('N1')
node3 = TreeNode('N2')
tree.insert(node1)
tree.insert(node2,parent=node1)
tree.insert(node3,parent=node2)

tree.root.disp()
print("Depth",tree.depth(node2))