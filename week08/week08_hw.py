# 231. 2的幂
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return n & (-n) == n


# 146. LRU 缓存机制
class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        # 哈希表，键存key,值存双向链表位置
        self.cache = dict()
        # 使用伪头部和伪尾部节点（注意是双向）
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        # 用来控制超出容量问题
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            # 如果key存在，先通过哈希表定位，然后移动到头部
            node = self.cache[key]
            self.moveToHead(node)
            return node.value

    def put(self, key: int, value: int) -> None:
        # 如果key存在，从哈希表获得双链表位置，然后修改节点的value，然后移动到头部
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
        else:
            # 如果key不存在，创建一个新的节点
            node = DLinkedNode(key, value)
            # 添加进哈希表
            self.cache[key] = node
            # 添加到头部
            self.addToHead(node)
            # 实际容量+1
            self.size += 1
            # 超出容量，删除双向链表的尾部节点
            if self.size > self.capacity:
                removed = self.removeTail()
                # 删除哈希表对应项
                self.cache.pop(removed.key)
                self.size -= 1

    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # 移动节点到头部由2个步骤进行[删除该节点]+[将该节点插入头部]
    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# 51. N 皇后
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(board, row_index):
            if row_index == n:
                board_list = list()
                for i in range(n):
                    b = ''.join(board[i])
                    board_list.append(b)
                res.append(board_list[:])

            for col in range(n):
                if not isValid(board, row_index, col):
                    continue
                board[row_index][col] = 'Q'
                backtrack(board, row_index + 1)
                # 撤销
                board[row_index][col] = '.'

        def isValid(board, row, col):
            # 检查列
            for i in range(n):
                if board[i][col] == 'Q':
                    return False
            # 检查右上
            i = row - 1
            j = col + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            # 检查左上
            i2 = row - 1
            j2 = col - 1
            while i2 >= 0 and j2 >= 0:
                if board[i2][j2] == 'Q':
                    return False
                i2 -= 1
                j2 -= 1
            return True

        def generateBoard(n):
            board = [[] for i in range(n)]
            for i in range(n):
                board[i] = list('.' * n)
            return board

        res = []
        board = generateBoard(n)
        backtrack(board, 0)
        return res