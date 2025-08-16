from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def display(self):
        lines, *_ = self._display_aux()
        #print("\n")
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

def build_tree_level_order(values):
    N = len(values)
    if N == 0:
        return TreeNode(None)
    q = deque()
    tree = TreeNode(values[0])
    q.append(tree)
    i=0
    while i < N and q:
        node = q.popleft()
        left_index = 2*i+1
        right_index = left_index + 1
        if left_index < N and values[left_index] is not None:
            node.left = TreeNode(values[left_index])
            q.append(node.left)
        if right_index < N and values[right_index] is not None:
            node.right = TreeNode(values[right_index])
            q.append(node.right)
        i += 1
    return tree

# search for a node in a BST
def search_bst(root, val):
    # base
    if root is None or root.val == val:
        return root

    # logic
    if root.val < val:
        node = search_bst(root.right, val)
    else:
        node = search_bst(root.left, val)
    return node

# convert tree to a list
def levelOrderTraversal(tree):
    q = deque()
    array=[]
    if not tree:
        return []
    q.append(tree)
    while q:
        node = q.popleft()
        #print(node.val, end = " --> ")
        array.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    #print(f"None")
    return array

class TreeNextNode(TreeNode):
    ''' This class is required for
    116 https://leetcode.com/problems/populating-next-right-pointers-in-each-node/ '''
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def build_tree_level_order_TreeNextNode(values):
    ''' Required for
    116 https://leetcode.com/problems/populating-next-right-pointers-in-each-node/ '''
    N = len(values)
    if N == 0:
        return TreeNextNode(None)
    q = deque()
    tree = TreeNextNode(values[0])
    q.append(tree)
    i=0
    while i < N and q:
        node = q.popleft()
        left_index = 2*i+1
        right_index = left_index + 1
        if left_index < N and values[left_index] is not None:
            node.left = TreeNextNode(values[left_index])
            q.append(node.left)
        if right_index < N and values[right_index] is not None:
            node.right = TreeNextNode(values[right_index])
            q.append(node.right)
        i += 1
    return tree

# convert tree to a list
def levelOrderTraversal_TreeNextNode(tree):
    ''' Required for
    116 https://leetcode.com/problems/populating-next-right-pointers-in-each-node/ '''
    if not tree:
        return []
    q = deque()
    array=[]
    q.append(tree)
    while q:
        node = q.popleft()

        curr = node
        while curr:
            array.append(curr.val)
            curr = curr.next
        array.append(None)

        if node.left:
            q.append(node.left)

    return array
