#TODO: fix all "left " to "leftChild" etc

class Node:
    def __init__(self, value, left = None, right = None, parent = None, color = None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color

class RedBlackTree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.nil = Node(None)
        self.nil.color = "black"

    def insert(self, value):
        self.size += 1
        temp = self.nil
        x = self.root
        
        if self.root is None:
            self.root = Node(value, self.nil, self.nil, self.nil, "black")
        else:
            node = Node(value, self.nil, self.nil, None, "red")
        

            #start at top of tree and work way down to nil
            while x is not self.nil:
                temp = x
                if (node.value < x.value):
                    x = x.left
                else:
                    x = x.right

            #set parent to previously met node
            node.parent = temp

            #if first node, put as root
            #if smaller than parent put to left
            #if larger than parent put to right
            if (temp == self.nil):
                self.root = node
            elif (node.value < temp.value):
                temp.left = node
            else:
                temp.right = node
            
            node.left = self.nil
            node.right = self.nil
            node.color = "red"

            self.insertFixup(node)

    def insertFixup(self, node):
        while node.parent.color == "red":
            if (node.parent == node.parent.parent.left):
                uncle = node.parent.parent.right
                #CASE 1: node uncle is RED
                if (uncle.color == "red"):
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    #CASE 2: node uncle is BLACK and node is a right child
                    if (node == node.parent.right):
                        node = node.parent
                        self.leftRotate(node)
                    #CASE 3: node uncle is BLACK and node is left child
                    node.parent.color = "black"
                    node.parent.parent.color = "black"
                    self.rightRotate(node.parent.parent)
            elif (node.parent == node.parent.parent.right):
                uncle = node.parent.parent.left
                #CASE 1: node uncle is RED
                if (uncle.color == "red"):
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    #CASE 2: node uncle is BLACK and node is a right child 
                    if (node == node.parent.left):
                        node = node.parent
                        self.rightRotate(node)
                    #CASE 3: node uncle is BLACK and node is left child
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.leftRotate(node.parent.parent)

        self.root.color = "black"

    def leftRotate(self, node):
        temp = node.right
        node.right = temp.left
        if (temp.left is not self.nil):
            temp.left.parent = node
        temp.parent = node.parent

        if (node.parent == self.nil):
            self.root = temp
        elif (node == node.parent.left):
            node.parent.left = temp
        else: 
            node.parent.right = temp
        temp.left = node
        node.parent = temp

    def rightRotate(self, node):
        temp = node.left
        node.left = temp.right
        if (temp.right is not self.nil):
            temp.right.parent = node
        temp.parent = node.parent

        if (node.parent == self.nil):
            self.root = temp
        elif (node == node.parent.right):
            node.parent.right = temp
        else: 
            node.parent.left = temp
        temp.right = node
        node.parent = temp

    def inorderWalk(self, root):
        if root != self.nil:
            self.inorderWalk(root.left)
            print(root.value, root.color)
            self.inorderWalk(root.right)

    def search(self, root, value):
        if (root is None or value == root.value):
            return root
        if (value < root.value):
            return self.search(root.left, value)
        else:
            return self.search(root.right, value)

    def transplant(self, u, v):
        if (u.parent == self.nil):
            self.root = v
        elif (u == u.parent.left):
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def treeMinimum(self, root):
        #if there is no more left to go, return the value
        if root.left is None or root.left is self.nil:
            return root
        #otherwise, keep moving left
        else:
            return self.treeMinimum(root.left)

    def delete(self, value):
        node = self.search(self.root, value)
        y = node
        yFirstColor = y.color

        if (node.left == self.nil):
            temp = node.right
            self.transplant(node, node.right)
        elif (node.right == self.nil):
            temp = node.left
            self.transplant(node, node.left)
        else:
            y = self.treeMinimum(node.right)
            yFirstColor = y.color
            temp = y.right
            if (y.parent == node):
                temp.parent = y
            else:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color
        if (yFirstColor == "black"):
            self.deleteFixup(temp)

    def deleteFixup(self, node):
        while node is not self.root and node.color == "black":
            #CASE 1: node sibling is RED
            if (node == node.parent.left):
                sibling = node.parent.right
                if (sibling.color == "red"):
                    sibling.color = "black"
                    node.parent.color = "red"
                    self.leftRotate(node.parent)
                #CASE 2: node sibling is BLACK and both siblings children are BLACK
                if (sibling.left.color == "black" and sibling.right.color == "black"):
                    sibling.color = "red"
                    node = node.parent
                else:
                    #CASE 3: node sibling is BLACK, sibling left child RED, sibling right child BLACK
                    if (sibling.right.color == "black"):
                        sibling.left.color = "black"
                        sibling.color = "red"
                        self.rightRotate(sibling)
                        sibling = node.parent.right
                    #CASE 4: node sibling is BLACK, sibling right child RED
                    else:
                        sibling.color = node.parent.color
                        node.parent.color = "black"
                        sibling.right.color = "black"
                        self.leftRotate(node.parent)
                        node = self.root
            elif (node == node.parent.right):
                sibling = node.parent.left
                #CASE 1: node sibling is RED
                if (sibling.color == "red"):
                    sibling.color = "black"
                    node.parent.color = "red"
                    self.rightRotate(node.parent)
                #CASE 2: node sibling is BLACK and both siblings children are BLACK
                if (sibling.right.color == "black" and sibling.left.color == "black"):
                    sibling.color = "red"
                    node = node.parent
                else:
                    #CASE 3: node sibling is BLACK, sibling left child RED, sibling right child BLACK
                    if (sibling.left.color == "black"):
                        sibling.right.color = "black"
                        sibling.color = "red"
                        self.leftRotate(sibling)
                        sibling = node.parent.left
                    #CASE 4: node sibling is BLACK, sibling right child RED
                    else:
                        sibling.color = node.parent.color
                        node.parent.color = "black"
                        sibling.right.color = "black"
                        self.rightRotate(node.parent)
                        node = self.root
        node.color = "black"
    
    
    
    
tree = RedBlackTree()



tree.insert(24)
tree.insert(90)
tree.insert(18)
tree.insert(13)
tree.insert(49)
tree.insert(22)
tree.insert(15)
tree.insert(100)
tree.insert(53)
tree.insert(45)
tree.insert(1)
tree.insert(19)
tree.insert(54)
tree.insert(55)
tree.insert(56)



tree.inorderWalk(tree.root)

tree.delete(19)
tree.delete(54)
tree.delete(15)

tree.inorderWalk(tree.root)