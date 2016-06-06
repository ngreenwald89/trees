class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        return self.pre_insert(self.root, new_val)
    
    def pre_insert(self, node, new_val):
        if new_val < node.value:
            if node.left:
                return self.pre_insert(node.left, new_val)
            node.left = Node(new_val)
            return True
        elif new_val > node.value:
            if node.right:
                return self.pre_insert(node.right, new_val)
            node.right = Node(new_val)
            return True
        return False

    def search(self, find_val):
        return self.pre_search(self.root, find_val)
        return False
    
    def pre_search(self, node, find_val):
        if node:
            if node.value == find_val:
                return True
            elif node.value < find_val:
                return self.pre_search(node.left, find_val)
            elif node.value > find_val:
                return self.pre_search(node.right, find_val)
        return False
                
    
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)