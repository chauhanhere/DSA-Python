from collections import deque
def levelorder_traversal(self,root):
        q=deque()
        q.append(root)
        res=[]
        while q:
            level=[]
            for i in range(len(q)):
                node=q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res
