# 70. 爬楼梯
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        else:
            f1 = 1
            f2 = 2
            for i in range(3,n+1):
                f3 = f1 + f2
                f1 = f2
                f2 = f3
            return f3

# 127. 单词接龙
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def addWord(word):
            if word not in wordId:
                nonlocal
                nodeNum
                wordId[word] = nodeNum
                nodeNum += 1

        def addEdge(word):
            addWord(word)
            id1 = wordId[word]
            chars = list(word)
            for i in range(len(word)):
                tmp = chars[i]
                chars[i] = '*'
                newWord = ''.join(chars)
                addWord(newWord)
                id2 = wordId[newWord]
                edge[id1].append(id2)
                edge[id2].append(id1)
                chars[i] = tmp

        wordId = dict()
        edge = collections.defaultdict(list)
        nodeNum = 0

        for word in wordList:
            addEdge(word)
        addEdge(beginWord)
        if endWord not in wordId:
            return 0

        disBegin = [float('inf')] * nodeNum
        beginId = wordId[beginWord]
        disBegin[beginId] = 0
        queBegin = collections.deque([beginId, ])

        disEnd = [float('inf')] * nodeNum
        endId = wordId[endWord]
        disEnd[endId] = 0
        queEnd = collections.deque([endId, ])

        while queBegin or queEnd:
            queBeginSize = len(queBegin)
            for _ in range(queBeginSize):
                nodeBegin = queBegin.popleft()
                if disEnd[nodeBegin] != float('inf'):
                    return (disBegin[nodeBegin] + disEnd[nodeBegin]) // 2 + 1
                for it in edge[nodeBegin]:
                    if disBegin[it] == float('inf'):
                        disBegin[it] = disBegin[nodeBegin] + 1
                        queBegin.append(it)
            queEndSize = len(queEnd)
            for _ in range(queEndSize):
                nodeEnd = queEnd.popleft()
                if disBegin[nodeEnd] != float('inf'):
                    return (disBegin[nodeEnd] + disEnd[nodeEnd]) // 2 + 1
                for it in edge[nodeEnd]:
                    if disEnd[it] == float('inf'):
                        disEnd[it] = disEnd[nodeEnd] + 1
                        queEnd.append(it)
        return 0

# 200. 岛屿数量
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(grid, i, j):
            # 设置边界
            neighbors = collections.deque([(i, j)])
            while neighbors:
                i, j = neighbors.popleft()
                for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '1':
                        neighbors.append((x, y))
                        grid[x][y] = '0'

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    bfs(grid, i, j)
                    count += 1
        return count
# 22. 括号生成
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = list()
        def backtrack(left,right,s):
            if left == n and right == n:
                res.append(s)
            s1 = s + '('
            s2 = s + ')'
            if left < n:
                backtrack(left+1,right,s1)
            if right < left:
                backtrack(left,right+1,s2)
        backtrack(0,0,'')
        return res