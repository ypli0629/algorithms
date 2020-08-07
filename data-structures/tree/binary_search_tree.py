"""
二叉搜索树
"""
from .binary_tree import BinaryTreeNode


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, value):
        """
        插入
        :param value:
        """
        if not self.root:
            self.root = BinaryTreeNode(value)
            return

        node = self.root
        while node:
            if value < node.value:
                if not node.left:
                    node.left = BinaryTreeNode(value)
                    return
                node = node.left
            else:
                if not node.right:
                    node.right = BinaryTreeNode(value)
                    return
                node = node.right
            pass
        pass

    def find(self, value):
        """
        查找
        :param value:
        :return:
        """
        if not self.root:
            return None

        node = self.root
        while node:
            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
            else:
                return node
        return node

    def inorder(self, node):
        """
        中序遍历
        """
        if not node:
            return
        yield from self.inorder(node.left)
        yield node
        yield from self.inorder(node.right)


if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)

    g = tree.inorder(tree.root)
    for node in [*g]:
        print(node.value)
