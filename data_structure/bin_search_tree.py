class BinarySearchTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def tree_sum(self):
        if self.left is None and self.right is None:
            return self.value
        elif self.left is None:
            return self.value + self.right.tree_sum()
        elif self.right is None:
            return self.value + self.left.tree_sum()
        else:
            return self.value + self.left.tree_sum() + self.right.tree_sum()
        
    def tree_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.tree_max()
        
    def tree_min(self):
        if self.left is None:
            return self.value
        else:
            return self.left.tree_min()
        
    def tree_height(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return self.right.tree_height() + 1
        elif self.right is None:
            return self.left.tree_height() + 1
        else:
            return max(self.left.tree_height(), self.right.tree_height()) + 1

    def __repr__(self):
        return f"(BSTree,root={self.value},left={self.left},right={self.right})"

    
tree = BinarySearchTree(5)
tree.insert(3)
tree.insert(8)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(9)
print(tree)
print(tree.tree_sum())
print(tree.tree_max())
print(tree.tree_min())
print(tree.tree_height())