class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left_node = None
        self.right_node = None
        self.height = 0


class AVLTree:
    root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, parent):
        if data < parent.data:
            if not parent.left_node:
                parent.left_node = Node(data, parent)
                self.handle_violation(parent.left_node)
            else:
                self.insert_node(data, parent.left_node)
        elif data > parent.data:
            if not parent.right_node:
                parent.right_node = Node(data, parent)
                self.handle_violation(parent.right_node)
            else:
                self.insert_node(data, parent.right_node)
        elif data > parent.data:
            pass

    def handle_violation(self, node):
        while node is not None:
            node.height = max(
                self.calculate_height(node.left_node),
                self.calculate_height(node.right_node)
            ) + 1
            self.violation_helper(node)
            node = node.parent

    def violation_helper(self, node):
        balance = self.calculate_balance(node)
        if balance > 1:
            if self.calculate_balance(node.left_node) < 0:
                self.left_rotate(node.left_node)
            self.right_rotate(node)
        elif balance < -1:
            if self.calculate_balance(node.right_node) > 0:
                self.right_rotate(node.right_node)
            self.left_rotate(node)

    def left_rotate(self, node):
        right_node = node.right_node
        if not node.parent:
            self.root = right_node
        else:
            parent = node.parent
            if parent.right_node == node:
                parent.right_node = right_node
            else:
                parent.left_node = right_node
        right_node.parent = node.parent
        node.parent = right_node
        node.right_node = right_node.left_node
        if right_node.left_node:
            right_node.left_node.parent = node
        right_node.left_node = node
        node.height = max(
            self.calculate_height(node.left_node),
            self.calculate_height(node.right_node)
        ) + 1
        right_node.height = max(
            self.calculate_height(right_node.left_node),
            self.calculate_height(right_node.right_node)
        ) + 1


    def right_rotate(self, node):
        left_node = node.left_node
        if not node.parent:
            self.root = left_node
        else:
            parent = node.parent
            if parent.right_node == node:
                parent.right_node = left_node
            else:
                parent.left_node = left_node
        left_node.parent = node.parent
        node.parent = left_node
        node.left_node = left_node.right_node
        if left_node.right_node:
            left_node.right_node.parent = node
        left_node.right_node = node
        node.height = max(
            self.calculate_height(node.left_node),
            self.calculate_height(node.right_node)
        ) + 1
        left_node.height = max(
            self.calculate_height(left_node.left_node),
            self.calculate_height(left_node.right_node)
        ) + 1

    def calculate_balance(self, node):
        return self.calculate_height(node.left_node) - self.calculate_height(node.right_node)

    def calculate_height(self, node):
        if node is None:
            return -1

        return node.height

    def remove(self, data):
        self.remove_node(data, self.root)

    def remove_node(self, data, node):
        if not node:
            return None

        if node.data > data:
            self.remove_node(data, node.left_node)
        elif node.data < data:
            self.remove_node(data, node.right_node)
        else:
            if not node.left_node and not node.right_node:
                parent = node.parent
                if parent.right_node == node:
                    parent.right_node=None
                if parent.left_node == node:
                    parent.left_node=None
                self.handle_violation(parent)
            elif not node.left_node and node.right_node:
                parent = node.parent
                node.right_node.parent = parent
                if parent:
                    if parent.right_node.data == node.data:
                        parent.right_node = node.right_node
                    else:
                        parent.left_node = node.right_node
                else:
                    node.right_node.parent = None
                    node.data = node.right_node.data
                self.handle_violation(parent)
            elif not node.right_node and node.left_node:
                parent = node.parent
                node.left_node.parent = parent
                if parent:
                    if parent.left_node.data == node.data:
                        parent.left_node = node.left_node
                    else:
                        parent.right_node = node.left_node
                else:
                    node.left_node.parent = None
                    node.data = node.left_node.data
                self.handle_violation(parent)
            else:
                leaf = node.left_node
                while leaf.right_node != None:
                    leaf = leaf.right_node

                leaf.data, node.data = node.data, leaf.data
                self.remove_node(leaf.data, leaf)
                self.handle_violation(node)

    def print(self):
        self.traverse(self.root)

    def find(self, data):
        return self.find_helper(data, self.root)

    def find_helper(self, data, node):
        if node:
            if data > node.data:
                return self.find_helper(data, node.right_node)
            elif data < node.data:
                return self.find_helper(data, node.left_node)
            else:
                return "Finded"
        else:
            return "No"

    def traverse(self, node):
        if node.left_node:
            self.traverse(node.left_node)
        if node.parent:
            print(node.data)
        else:
            print(node.data)

        if node.right_node:
            self.traverse(node.right_node)

