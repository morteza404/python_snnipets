class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def tree_sum(self, root):
        if root is None:
            return 0
        return self.tree_sum(root.left) + self.tree_sum(root.right)

    def __str__(self):
        return str(self.value)
    
    
    
tree = Tree(5)
tree.left = Tree(3)
tree.right = Tree(8)
tree.left.left = Tree(2)
tree.left.right = Tree(4)
tree.right.left = Tree(6)
tree.right.right = Tree(9)
print(tree.tree_sum())