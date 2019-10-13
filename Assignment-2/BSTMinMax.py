#node with pointers to left and right children and a value (key) inside
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value

#insert a node to the left or right of a node
#maintaining the BST properties
def insert(root, node):
    #if there is no root, the root is equal to the node
    #Although this should technichally never run, based on the way I build my tree
    if root is None:
        root = node
    
    #move down right side of tree if value is larger than root of tree
    if (root.value < node.value):
         #if there is currently no node to the right, place node there
        #set parent to the current root node
        if (root.right is None):
            root.right = node
            node.parent = root
        else:
            #if there is a node there, start from that node and repeat process
            insert(root.right, node)
    #move down left side of tree if value is smaller than root of tree   
    elif (root.value > node.value):
        #if there is currently no node to the left, place node there
        #set parent to the current root node
        if (root.left is None):
            root.left = node
            node.parent = root
        else:
            #if there is a node there, start from that node and repeat process
            insert(root.left, node)

def inorderWalk(root):
    if root != None:
        #go down and print left (smallest side) of tree
        inorderWalk(root.left)
        #once walked down, start printing
        print(root.value)
        #once all the way down left, go down right side and do the same
        inorderWalk(root.right)

def treeMinimum(root):
    #if there is no more left to go, return the value
    if root.left is None:
        return root.value
    #otherwise, keep moving left
    else:
        return treeMinimum(root.left)

def treeMaximum(root):
    #if there is no more right to go, return the value
    if root.right is None:
        return root.value
    #otherwise, keep moving right
    else:
        return treeMaximum(root.right)


rootNode = Node(50)

insert(rootNode, Node(30))
insert(rootNode, Node(20))
insert(rootNode, Node(40))
insert(rootNode, Node(70))
insert(rootNode, Node(60))
insert(rootNode, Node(80))


inorderWalk(rootNode)

print("Minimum: "+ str(treeMinimum(rootNode)))
print("Maximum: "+ str(treeMaximum(rootNode)))
