class Solution:
    def preorder(self,root) :
        output=[]
        def helper(node):
            if not node:
                return None
            output.append(node.val)
            for i in node.children:
                helper(i)
        helper(root)
        return output
        
# 迭代
class Solution:
    def preorder(self,root):
        ans = []
        stack = [root]
        if not root:
            return ans
        while stack :
            n = stack.pop()
            ans.append(n.val)
            if n.children:
                for i in n.children[::-1]:
                    stack.append(i)
        return ans