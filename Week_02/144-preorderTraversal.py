class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        def helper(root):
            if not root:
                return
            ans.append(root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        return ans
        
# 迭代
#class Solution:
#    def preorderTraversal(self, root: TreeNode) -> List[int]:
#        ans= []
#        stack = []
#        if root is None:
#            return ans
#        while root or len(stack)>0:
#            if root:
#                stack.append(root)
#                ans.append(root.val)
#                root = root.left
#            else:
#                n = stack.pop(-1)
#                if n.right != None:
#                    root = n.right
#        return ans