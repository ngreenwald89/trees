class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        return self.preorder_search(tree.root, find_val)

    def print_tree(self):
        return self.preorder_print(tree.root, "")[:-1]

    def preorder_search(self, start, find_val):
        print('Doing check')
        if start:
            print('has value', start.value)
            if start.value == find_val:
                return True
            else:
                # or operator: reads left to right. if left object is false, returns the right one. if left is true, returns the left one.
                # will keep going until a True object is found, which is found. Likewise, if all False last False is returned
                return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
        print('no value')
        return False

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

tree.print_tree()