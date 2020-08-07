from collections import deque


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder(root):
    """
    先序遍历
    :param root:
    :return:
    """
    if not root:
        return
    print(root.value)
    preorder(root.left)
    preorder(root.right)
    pass


def inorder(root):
    """
    中序遍历
    :param root:
    :return:
    """
    if not root:
        return
    inorder(root.left)
    print(root.value)
    inorder(root.right)
    pass


def postorder(root):
    """
    后序遍历
    :param root:
    :return:
    """
    if not root:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.value)
    pass


def levelorder(root):
    """
    广度优先遍历
    :param root:
    """
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        element = queue.popleft()
        print(element.value)
        if element.left:
            queue.append(element.left)
        if element.right:
            queue.append(element.right)
        pass


if __name__ == '__main__':
    tree = BinaryTreeNode(1)
    tree.left = BinaryTreeNode(2)
    tree.right = BinaryTreeNode(3)
    tree.left.left = BinaryTreeNode(4)
    tree.left.right = BinaryTreeNode(5)
    tree.right.left = BinaryTreeNode(6)
    tree.right.right = BinaryTreeNode(7)

    # preorder(tree)
    # inorder(tree)
    # postorder(tree)
    levelorder(tree)
