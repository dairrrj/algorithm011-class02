class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans=[]
        def recursion(root):
            if not root:
                return
            recursion(root.left)
            ans.append(root.val)
            recursion(root.right)
        recursion(root)
        return ans
        
# 迭代
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans= []
        stack = []
        if root is None:
            return ans
        while root or len(stack)>0:
            if root:
                stack.append(root)
                root = root.left
            else:
                n = stack.pop(-1)
                ans.append(n.val)
                if n.right != None:
                    root = n.right
        return ans