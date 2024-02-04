'''
Writing EX
1.   
a)   
Preorder: D B A C F E G   
Inorder: A B C D E F G   
Postorder: A C B E G F D   
b)   
Preorder: C B A D E   
Inorder: A B C D E   
Postorder: A B C E D    
c)   
Preorder: E C B A D H F G I   
Inorder: A B C D E F G H I   
Postorder: A B D C G F I H E   

2.1 Trước khi xóa   
Preorder: 4 3 1 11 5 9 2 6 15 12      
Inorder: 1 2 3 4 5 6 9 11 12 15   
Postorder: 1 2 3 6 9 5 12 15 11 4   

2.1 Sau khi xóa   
Preorder: 4 1 5 9 6 15 12   
Inorder: 1 4 5 6 9 12 15   
Postorder: 1 6 9 12 15 5 4   

2.2 Trước khi xóa   
Preorder: 12 7 1 3 2 5 10 8 6 9   
Inorder: 1 2 3 5 6 7 8 9 10 12   
Postorder: 2 3 5 1 6 9 8 10 7 12   

2.2 Sau khi xóa   
Preorder: 12 1 2 3 10 8 9   
Inorder: 1 2 3 8 9 10 12   
Postorder: 2 3 1 9 8 10 12   

3.1   
Preorder: 4 3 1 2 11 5 9 6 15 12   
Inorder: 1 2 3 4 5 6 9 11 12 15   
Postorder: 2 1 3 6 9 5 12 15 11 4   
Level-order: 4 3 11 1 5 15 2 9 12 6   

3.2   
Preorder: 12 7 1 3 2 5 10 8 6 9   
Inorder: 1 2 3 5 7 6 8 9 10 12   
Postorder: 2 3 5 1 6 9 8 10 7 12   
Level-order: 12 7 10 1 8 9 3 5 6
4.   
Sau khi thực hiện thao tác xóa, chúng ta cần cập nhật chiều cao của các nút và kiểm tra xem cây có bị mất cân đối không. Nếu cây mất cân đối, chúng ta cần xác định nút mất cân đối đầu tiên khi đi từ nút đã xóa lên nút gốc.   
Dựa vào nút mất cân đối và nút con của nó, chúng ta cần xác định đây là trường hợp xoay nào trong 4 trường hợp: Left-Left, Left-Right, Right-Right, Right-Left.   
Tùy thuộc vào trường hợp xoay, chúng ta sẽ thực hiện xoay trái, xoay phải, hoặc cả hai để làm cân đối lại cây.   
5.   
a. Một cây nhị phân gần như hoàn chỉnh là một cây nhị phân đầy đủ khi mỗi nút trong cây có 0 hoặc 2 nút con. Điều này có nghĩa là đối với một cây nhị phân đầy đủ có I nút nội bộ, số lượng lá là L = I + 1. Do đó, tổng số nút N trong một cây nhị phân đầy đủ là N = 2I + 1. Vì vậy, để một cây nhị phân gần như hoàn chỉnh trở thành một cây nhị phân đầy đủ, tổng số nút n phải là một số lẻ.   
b. Một cây nhị phân gần như hoàn chỉnh là một cây nhị phân hoàn chỉnh (hoặc hoàn hảo) khi tất cả các cấp của cây đều được điền đầy. Điều này có nghĩa là đối với một cây nhị phân hoàn chỉnh có chiều cao h, tổng số nút N là N = 2^h - 1. Vì vậy, để một cây nhị phân gần như hoàn chỉnh trở thành một cây nhị phân hoàn chỉnh, tổng số nút n phải nhỏ hơn một đơn vị so với một lũy thừa của 2.   
6.   
Sau khi kiểm tra nút 2, chúng ta biết rằng 57 lớn hơn 2, vì vậy chúng ta sẽ di chuyển sang nút con bên phải của nút 2. Tuy nhiên, trong chuỗi, nút tiếp theo lại là 90, điều này không thể xảy ra vì 90 lớn hơn 57. Do đó, chuỗi nút được kiểm tra 2, 90, 63, 70, 68, 72, 57 không thể xảy ra khi tìm kiếm số 57 trong cây tìm kiếm nhị phân.
'''
class Node:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None
class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,x):
        self.queue.append(x)
    def dequeue(self):
        return self.queue.pop(0)
    def show(self):
        for q in self.queue:
            print(q)
    def is_empty(self):
        return self.queue==[]
class BSTree:
    def __init__(self):
        self.root=None
    def isEmpty(self):
        return self.root==None
    def clear(self):
        self.root=None
    def search(self,x):
        if self.isEmpty():
            return
        cur=self.root
        while cur:
            if cur.data==x:
                return cur
            elif cur.data>x:
                cur=cur.left
            else:
                cur=cur.right
    def insert(self,x):
        new=Node(x)
        if self.isEmpty():
            self.root=new
        cur=self.root
        while cur:
            if cur.data==x:
                return
            elif cur.data>x:
                if cur.left is None:
                    cur.left=new
                    break
                else:
                    cur=cur.left
            else:
                if cur.right is None:
                    cur.right=new
                    break
                else:
                    cur=cur.right
    def breath(self):
        if self.isEmpty():
            return
        queue=Queue()
        queue.enqueue(self.root)
        res=[]
        while not queue.is_empty():
            node=queue.dequeue()
            res.append(node.data)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return res
    def preorder(self,p):
        if p is None:
            return
        print(p.data, end=' ')
        self.preorder(p.left)
        self.preorder(p.right)
    def inorder(self,p):
        if p==None:
            return
        self.inorder(p.left)
        print(p.data, end=' ')
        self.inorder(p.right)
    def postorder(self,p):
        if p==None:
            return
        self.postorder(p.left)
        self.postorder(p.right)
        print(p.data, end=' ')
    def count(self):
        return len(self.breath())
    def dele(self,x):
        if self.isEmpty():
            return 
        cur=self.root
        father=None
        while cur:
            if cur.data==x:
                cur=None
            elif cur.data>x:
                cur=cur.left
            else:
                cur=cur.right
        return
    def min(self):
        return min(self.breath())
    def max(self):
        return max(self.breath())
    def sum(self):
        return sum(self.breath())
    def avg(self):
        return sum(self.breath())/len(self.breath())
    def height(self):
        if self.root is None:
            return -1
        queue = Queue()
        queue.enqueue((self.root, 0))
        while not queue.is_empty():
            node, depth = queue.dequeue()
            if node.left:
                queue.enqueue((node.left, depth + 1))
            if node.right:
                queue.enqueue((node.right, depth + 1))
        return depth
    def cost(self):
        if self.root is None:
            return 0
        queue = Queue()
        queue.enqueue((self.root, self.root.val))
        max_cost = 0
        while not queue.is_empty():
            node, cost = queue.dequeue()
            if node.left:
                queue.enqueue((node.left, cost + node.left.val))
            if node.right:
                queue.enqueue((node.right, cost + node.right.val))
            if not node.left and not node.right:
                max_cost = max(max_cost, cost)
        return max_cost
    def isAVL(self):
        def check(node):
            if node is None:
                return 0, True
            left_height, left_balanced = check(node.left)
            right_height, right_balanced = check(node.right)
            return max(left_height, right_height) + 1, left_balanced and right_balanced and abs(left_height - right_height) <= 1
        return check(self.root)
'''18
For tree 3.1, the traversals are:

Preorder: 4 3 1 2 11 5 9 6 15 12
Inorder: 1 2 3 4 5 6 9 11 12 15
Postorder: 2 1 3 6 9 5 12 15 11 4
Level-order: 4 3 11 1 5 15 2 9 12 6

For tree 3.2, the traversals are:

Preorder: 12 7 1 3 2 5 10 8 6 9
Inorder: 1 2 3 5 7 6 8 9 10 12
Postorder: 2 3 5 1 6 9 8 10 7 12
Level-order: 12 7 10 1 8 9 3 5 6
'''
def isHeap(root):
    def isComplete(root, index, node_count):
        if root is None:
            return True
        if index >= node_count:
            return False
        return (isComplete(root.left, 2 * index + 1, node_count) and
                isComplete(root.right, 2 * index + 2, node_count))

    def isHeapUtil(root):
        if root.left is None and root.right is None:
            return True
        if root.right is None:
            return root.data >= root.left.data
        else:
            if root.data >= root.left.data and root.data >= root.right.data:
                return isHeapUtil(root.left) and isHeapUtil(root.right)
            else:
                return False

    node_count = countNodes(root)
    if isComplete(root, 0, node_count) and isHeapUtil(root):
        return True
    return False
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        else:
            if root.val < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)

    def search(self, root, key):
        if root is None or root.val == key:
            return root
        if root.val < key:
            return self.search(root.right, key)
        return self.search(root.left, key)