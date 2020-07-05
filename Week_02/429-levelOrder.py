class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        queue = [root]
        ans = []
        while queue:
            level_ans = []
            for i in range(len(queue)):
                n = queue.pop(0)
                level_ans.append(n.val)
                if n.children:
                    queue += n.children
            ans.append(level_ans)
        return ans