学习笔记
* 递归
递归是有模板的，但是难点在于如何找把问题分解成子问题，每一层要重复的一样的东西是什么，传递到下一层返回给上一层什么？drill down和process logic的处理顺序不一定？
爬楼梯问题：分解成子问题是上到第n层只有两种方法，一种是跨一步一种是跨两步，跨一步就是到达n-1台阶时有的方法总数加上到达n-2级台阶时有的方法。
兔子繁殖问题：第n天的兔子数=第n-1天的兔子数量（原本有的）+第n-2天的兔子数量（n-1天只有这么多兔子能生，新增加的小兔子）
从前序与中序遍历序列构造二叉树：递归的子问题不太好理解。
```
#终止条件
没有左子树
#process logic
有左子树，前序的第一个点即为根节点添加根节点，在中序遍历中找到根节点的索引，确定左右子树的大小和位置，中序左边的都是左子树右边都是右子树
#drill down
递归的构建左子树和右子树
root.left = 递归函数（preorder[左子树]，inorder[左子树])
root.right = 递归函数（preorder[右子树]，inorder[右子树])
```

```
def recursion(level):
	if level > max:
		process_result
		return
	
	process(level,data,...)
	
	recursion(level+1)
	# reverse if needed
```